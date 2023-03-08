import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def money_depression_relationship(data: pd.DataFrame):
    data = data[["gained_asset", "depressed", "durable_asset", "save_asset"]]
    gained_asset = data[["gained_asset"][0]]
    depression_status = data[["depressed"][0]]
    durable_asset = data[["durable_asset"][0]]
    save_asset = data[["save_asset"][0]]
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
    ax1.hist(gained_asset, bins=5, color='green', alpha=0.5, label='Non-depressed')
    ax1.hist([gained_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=5, color='blue', alpha=0.5, label='Depressed')
    ax1.set_xlabel('durable_asset')
    ax1.set_ylabel('Depressed')
    ax2.hist(durable_asset, bins=5, color='green', alpha=0.5, label='Non-depressed')
    ax2.hist([durable_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=5, color='blue', alpha=0.5, label='Depressed')
    ax2.set_xlabel('durable_asset')
    ax2.set_ylabel('Depressed')
    ax3.hist(save_asset, bins=5, color='green', alpha=0.5, label='Non-depressed')
    ax3.hist([save_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=5, color='blue', alpha=0.5, label='Depressed')
    ax3.set_xlabel('save_asset')
    ax3.set_ylabel('Depressed')

    data = data[["gained_asset", "durable_asset", "save_asset"]]
    data = get_precent(gained_asset, depression_status)
    print(data)
    sns.lineplot(data=data, x="income", y="percentage")
    plt.show()


def get_precent(data, depression):
    depression_num = [0, 0, 0, 0, 0]
    total_num = [0, 0, 0, 0, 0]
    percentage = [0, 0, 0, 0, 0]
    for i in range(len(data)):
        if depression[i] == 1:
            depression_num[round(data[i] // 20000000)] += 1
        total_num[round(data[i] // 20000000)] += 1
    for i in range(len(depression_num)):
        percentage[i] = depression_num[i] / total_num[i]
    data = {'percentage': percentage,
            'income': [0.2, 0.4, 0.6, 0.8, 1.0]}
    return data


def main():
    data = pd.read_csv('dateset/b_depressed.csv')
    money_depression_relationship(data)


if __name__ == '__main__':
    main()
