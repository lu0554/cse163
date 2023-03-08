import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def education_depression_relationship(data: pd.DataFrame):
    data = data[["education_level", "depressed"]]
    education_level = data[["education_level"][0]]
    depression_status = data[["depressed"][0]]
    plt.hist(education_level, bins=40, color='green', alpha=0.5, label='Non-depressed')
    plt.hist([education_level[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=40, color='blue', alpha=0.5, label='Depressed')
    plt.xlabel("Education Level")
    plt.ylabel("Number of people")
    plt.tight_layout()
    plt.savefig("education.png")
    percentage = get_education_percent(education_level, depression_status)
    print(percentage)
    sns.lineplot(data=percentage, x="education_level", y="percentage")
    plt.savefig("percent.png")

def money_depression_relationship(data: pd.DataFrame):
    data = data[["gained_asset", "depressed", "durable_asset", "save_asset"]]
    gained_asset = data[["gained_asset"][0]]
    depression_status = data[["depressed"][0]]
    durable_asset = data[["durable_asset"][0]]
    save_asset = data[["save_asset"][0]]
    total = data[["gained_asset"][0]] + data[["depressed"][0]] + data[["save_asset"][0]]
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
    ax1.hist(gained_asset, bins=25, color='green', alpha=0.5, label='Non-depressed')
    ax1.hist([gained_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=25, color='blue', alpha=0.5, label='Depressed')
    ax1.set_xlabel('gained_asset')
    ax1.set_ylabel('Depressed')
    ax2.hist(durable_asset, bins=25, color='green', alpha=0.5, label='Non-depressed')
    ax2.hist([durable_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=25, color='blue', alpha=0.5, label='Depressed')
    ax2.set_xlabel('durable_asset')
    ax2.set_ylabel('Depressed')
    ax3.hist(save_asset, bins=25, color='green', alpha=0.5, label='Non-depressed')
    ax3.hist([save_asset[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=25, color='blue', alpha=0.5, label='Depressed')
    ax3.set_xlabel('save_asset')
    ax3.set_ylabel('Depressed')
    ax4.hist(total, bins=25, color='green', alpha=0.5, label='Non-depressed')
    ax4.hist([total[i] for i in range(len(depression_status)) if depression_status[i] == 1],
             bins=25, color='blue', alpha=0.5, label='Depressed')
    ax4.set_xlabel('total')
    ax4.set_ylabel('Depressed')
    plt.tight_layout()
    plt.savefig("asset_depression.png")
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
    data = get_precent(gained_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax1)
    ax1.set_xlabel('Gained asset')
    ax1.set_ylabel('Depressed Percentage')
    data = get_precent(durable_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax2)
    ax2.set_xlabel('Durable asset')
    ax2.set_ylabel('Depressed Percentage')
    data = get_precent(save_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax3)
    ax3.set_xlabel('Save asset')
    ax3.set_ylabel('Depressed Percentage')
    plt.tight_layout()
    plt.savefig("percentage_asset")

def get_education_percent(data, depression):
    depression_num = [0] * 20
    total_num = [0] * 20
    percentage = [0] * 20
    for i in range(len(data)):
        if depression[i] == 1:
            depression_num[data[i]] += 1
        total_num[data[i]] += 1
    for i in range(len(depression_num)):
        if total_num[i] != 0:
            percentage[i] = depression_num[i] / total_num[i]
    data = {'percentage': percentage,
            'education_level': list(range(1, 21))}
    return data
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
            'income': [20000000, 40000000, 60000000, 80000000, 100000000]}
    return data


def main():
    data = pd.read_csv('dateset/b_depressed.csv')
    money_depression_relationship(data)
    education_depression_relationship(data)


if __name__ == '__main__':
    main()
