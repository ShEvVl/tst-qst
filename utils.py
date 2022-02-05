import random
import pandas as pd

# read csv file
with open("info.csv", "r", encoding="utf8") as f:
    lines = f.readlines()

data = []

# formatting data to build pd.table
for i, line in enumerate(lines):
    data.append(line.replace("\n", ""))
df = pd.Series(data).str.split(pat=";", expand=True)
df.columns = ["url", "amount_of_shows"] + [f"category{x}" for x in range(1, 11)]
df["amount_of_shows"] = df["amount_of_shows"].astype(int)

# pick up all available labels of categories
req = list(set(df.iloc[:, 2:].values.flatten()))
req = list(filter(None, req))


# log file to collect index of previous picture
log_ind = []


def output(cats_list):
    """The output function

    Args:
        cats_list (list): list of available categories

    Returns:
        url (str): url path of img in static
        log (list): indexes of img of previous view
        credits (int): amount of shows of url image
    """
    seq = []

    # if categories not chosen
    if cats_list == []:
        url = df.iloc[random.randint(0, len(df) - 1), 0]
        ind_url = df.index[df["url"] == url].tolist()
        log_ind.append(ind_url[0])
    else:

        # serching string with chosen categories
        for cats in cats_list:
            for k in range(10):
                cat_string = df.index[df[f"category{k + 1}"] == cats].tolist()
                if cat_string == []:
                    pass
                else:
                    seq.append(cat_string)

        # make df uniq
        seq_u = list(set([item for sublist in seq for item in sublist]))

        # sorting df by amount of shows
        df_temp = df.iloc[seq_u].sort_values(by=["amount_of_shows"], ascending=False)

        # get url from top string of df
        url = df_temp.iloc[0, 0]

        # get index
        ind_url = df.index[df["url"] == url].tolist()

        # if log list is empty
        if log_ind == []:
            pass
        else:

            # changing img if previous img the same
            if ind_url[0] == log_ind[-1]:
                rand_ind = random.randint(0, len(df_temp) - 1)

                # repeat operation until missmatch
                while log_ind[-1] == rand_ind:
                    rand_ind = random.randint(0, len(df_temp) - 1)
                else:
                    url = df_temp.iloc[rand_ind, 0]
                    ind_url = df.index[df["url"] == url].tolist()

        # logging index
        log_ind.append(ind_url[0])

        # change amount of shows to -1
        df.iloc[ind_url, 1] = df.iloc[ind_url, 1] - 1
    return url, log_ind, df.iloc[ind_url, 1].values[0]
