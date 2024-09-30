import pandas as pd
import seaborn as  sns
import openpyxl
import matplotlib.pyplot as plt


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

key_all_sales = total_sales_per_product(x).keys();
val_all_sales = total_sales_per_product(x).values();
sns.barplot(x=key_all_sales, y=val_all_sales);

key_date_sales = sales_over_time(x).keys();
val_sdate_ales = sales_over_time(x).values();
sns.barplot(x=key_date_sales, y=val_sdate_ales);
plt.xticks(rotation=45);
