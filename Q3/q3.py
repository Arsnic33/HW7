import pandas as pd

def main():
    data = {'unit price': [1000, 280, 900],
            'number': [25,120,30]
            ,'Name' : ["store1","store2","store3"]}
    df = pd.DataFrame(data)
    df.set_index('Name', inplace=True)


    print("데이터프레임 생성:")
    print(df.to_string(index_names=False))

    df['total price'] = df['unit price'] * df['number']
    print("\n총 가격이 추가된 데이터프레임:")
    print(df.to_string(index_names=False))

    top_stores = df.nlargest(2, 'total price')
    top_removed = top_stores.drop(columns=['total price'])
    print("\n총 가격이 가장 비싼 가게 2개:")
    print(top_removed.to_string(index_names=False)   )
    
if __name__ == "__main__":
    main()
    
