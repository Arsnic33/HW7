import pandas as pd

def main():
    df = pd.read_csv('gender2.csv', encoding= 'euc-kr', index_col=0)
    df_new = df[['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']].copy()
    df_new.columns = ['Total', 'Male', 'Female']
    print(df_new)

if __name__ == "__main__":
    main()
