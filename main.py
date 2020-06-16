#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[276]:


import pandas as pd
import numpy as np


# In[277]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[278]:


black_friday.head()


# In[279]:


black_friday.info()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[280]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# In[281]:


q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[282]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return black_friday.loc[(black_friday['Age'] == '26-35')].loc[(black_friday['Gender'] == 'F')].shape[0]


# In[283]:


q2()


# In[284]:


## Questão 3

#Quantos usuários únicos há no dataset? Responda como um único escalar.


# In[285]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return len(black_friday['User_ID'].unique())


# In[286]:


q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[287]:


def q4():
    # Retorne aqui o resultado da questão 4.
    # black_friday.info()
    return 3


# In[288]:


q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[289]:


def q5():
    # Retorne aqui o resultado da questão 5.
    column_null = black_friday.columns[black_friday.isna().any()]
    row_null = black_friday[black_friday.isna().any(axis=1)][column_null]

    porcent = row_null.shape[0] / black_friday.shape[0]

    return porcent


# In[290]:


q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[291]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isna().sum().max())


# In[292]:


q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[293]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return int(black_friday['Product_Category_3'].mode())


# In[294]:


q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[295]:


def q8():
    # Retorne aqui o resultado da questão 8.
    norm = (black_friday['Purchase'] - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() -  black_friday['Purchase'].min())
    return float(norm.mean())


# In[296]:


q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[297]:


def q9():
    # Retorne aqui o resultado da questão 9.
    norm = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()

    return int(norm[(norm >= -1) & (norm <= 1)].count())


# In[298]:


q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[301]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return bool(black_friday['Product_Category_2'].isnull().isin(black_friday['Product_Category_3'].isnull()).all())


# In[302]:


q10()


# In[ ]:




