from utils import *


def save_review_keyword():
    url_dict = {}
    # url_dict["strange_girl1"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=31726&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["strange_girl2"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=128273&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    
    # url_dict["with_god1"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=85579&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["with_god2"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=167697&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    
    # url_dict["spiderman1"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=135874&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["spiderman2"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=173123&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["spiderman3"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=208077&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    
    # url_dict["harry_potter2"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=33930&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["harry_potter3"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=35546&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["harry_potter5"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=57095&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["harry_potter6"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=67900&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["harry_potter7"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=67901&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'

    # url_dict["kingsman1"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=114249&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["kingsman2"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=149747&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'
    # url_dict["kingsman3"] = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=159893&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'

    for name, url in url_dict.items():
        save_review_from_url(url, name)
        save_noun_from_txt(name)


def similarity_from_name():
    name1 = "kingsman1"
    name2 = "kingsman2"
    similarity = compute_similarity(name1, name2)
    print(similarity)


if __name__ == "__main__":
    save_review_keyword()
    similarity_from_name()
