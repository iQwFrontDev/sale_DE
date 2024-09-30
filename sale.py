import pandas as pd
def read_sales_data(file_path):
    return pd.read_excel(file_path).to_dict()



def total_sales_per_product(sales_data):

    df = pd.DataFrame(sales_data)
    df['sum'] = df['quantity'] * df['price']
    df = df.groupby('product_name')['sum'].sum()
    return df.to_dict()


def sales_over_time(sales_data):
    df = pd.DataFrame(sales_data)
    df['sum'] = df['quantity'] * df['price']
    df = df.groupby('date')['sum'].sum()
    return df.to_dict()


x = read_sales_data('/home/user/sale_DE/sale_DE/Book1.xlsx')
print(total_sales_per_product(x))
print(sales_over_time(x))