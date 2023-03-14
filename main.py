import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
sns.set()


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
    fig, ax = plt.subplots(3)
    data = get_precent(gained_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax[0])
    ax[0].set_xlabel('Gained asset')
    ax[0].set_ylabel('Depressed Percentage')
    data = get_precent(durable_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax[1])
    ax[1].set_xlabel('Durable asset')
    ax[1].set_ylabel('Depressed Percentage')
    data = get_precent(save_asset, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax[2])
    ax[2].set_xlabel('Save asset')
    ax[2].set_ylabel('Depressed Percentage')
    plt.tight_layout()
    plt.savefig("percentage_asset")


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


def sex_freq(df):
    pd.crosstab(df.sex, df.depressed).plot(kind="bar", figsize=(20, 5))
    plt.title('Depressed Frequency for Sex')
    plt.xlabel('Sex (0 = Female, 1 = Male)')
    plt.xticks(rotation=0)
    plt.legend(["Haven't Depressed", "Have Depressed"])
    plt.ylabel('Frequency')
    plt.savefig("sexFreq.png")


def logistic_model(df):
    df = df.dropna()
    X = df.loc[:, df.columns != 'depressed']
    X = pd.get_dummies(X)
    y = df.depressed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy score:", accuracy_score(y_test, y_pred))
    print("Precision score:", precision_score(y_test, y_pred))


def education_freq(df):
    pd.crosstab(df.education_level, df.depressed).plot(kind="bar", figsize=(20, 8))
    plt.title('Depressed Frequency for education level')
    plt.xlabel('education level')
    plt.ylabel('Frequency')
    plt.savefig('depressedVsEducation.png')


def number_children(df):
    pd.crosstab(df.Number_children, df.depressed).plot(kind="bar", figsize=(20, 8))
    plt.title('Depressed Frequency for number children')
    plt.xlabel('Number children')
    plt.ylabel('Frequency')
    plt.savefig('childrenNumberVsEducation.png')


def living_expenses(df):
    depression_status = df[["depressed"][0]]
    living_expense = df.living_expenses
    fig, ax = plt.subplots(2)
    ax[0].hist(living_expense, bins=25, color='green', alpha=0.5, label='Non-depressed')
    ax[0].hist([living_expense[i] for i in range(len(depression_status)) if depression_status[i] == 1],
               bins=25, color='blue', alpha=0.5, label='Depressed')
    ax[0].set_xlabel('living_expenses')
    ax[0].set_ylabel('Depressed')
    data = get_precent(living_expense, depression_status)
    sns.lineplot(data=data, x="income", y="percentage", ax=ax[1])
    plt.xlabel("expense")
    plt.savefig("livingExpenseVsDepression.png")


def main():
    data = pd.read_csv("dateset/b_depressed.csv")
    money_depression_relationship(data)
    sex_freq(data)
    education_freq((data))
    logistic_model(data)
    number_children(data)
    living_expenses(data)


if __name__ == '__main__':
    main()