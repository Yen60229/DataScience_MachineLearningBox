import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules



dataset = [
  ['Milk', 'Onion', 'Nutmeg', 'Kidney' 'Beans', 'Eggs', 'Yogurt'],
  ['Dill', 'Onion', 'Nutmeg', 'Kidney' 'Beans', 'Eggs', 'Yogurt'],
  ['Milk', 'Apple', 'Kidney' 'Beans', 'Eggs'],
  ['Milk', 'Unicorn', 'Corn', 'Kidney' 'Beans', 'Yogurt'],
  ['Corn', 'Onion', 'Onion', 'Kidney' 'Beans', 'Ice cream', 'Eggs'],
]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

#Apriori
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
### alternatively:
#frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)
#frequent_itemsets = fpmax(df, min_support=0.6, use_colnames=True)
frequent_itemsets.sort_values('support', ascending=False, inplace=True)
print(frequent_itemsets)

# Association Rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
rules.sort_values('confidence', ascending=False, inplace=True)
print(rules[['antecedents', 'consequents', 'support', 'confidence']])
