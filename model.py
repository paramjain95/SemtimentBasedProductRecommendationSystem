# import libraties
import pickle
import pandas as pd

data = pickle.load(open('data','rb'))

def predict_sentiment(reviews):
    vectoriser= pickle.load(open('tfidf_vectoriser.sav','rb'))
    x_input = vectoriser.transform(reviews['reviews_text'])
    model = pickle.load(open('final_model.sav','rb'))
    y_pred= model.predict(x_input)
    y_pred_series = pd.Series(y_pred)
    positive_percent = round(y_pred_series.value_counts(normalize=True),2)['Positive']
    return positive_percent


def recommend_product(user):
    product_sentiment_dict={}
    user_final_rating = pickle.load(open("final_recommendation_system",'rb'))
    recommend_products = user_final_rating.loc[user].sort_values(ascending=False)[0:20]

    for item in recommend_products.index:
        reviews = data[data['name'] == item]
        positive_percent = predict_sentiment(reviews)
        product_sentiment_dict[item] = positive_percent
    sorted_dict = sorted(product_sentiment_dict.items(), key=lambda x: x[1], reverse=True)
    top5 = []
    for item in sorted_dict[:5]:
        top5.append(item[0])
    return top5

def get_all_username():
    user_name = data['reviews_username']
    user_name = user_name.to_list()
    return user_name