# coding=utf-8


def extract_from_dictionary_by_string_in_key(dictionary, string):
    """
    Function extracts dict items that have string in key
    :param dict:
    :param subkey:
    :return extracted_dictonary:
    """
    #   predefined empty string to store new items
    extracted_dictonary = {}
    # print "------------------------------"
    # print string
    # print "input =", dictionary
    for key in dictionary:
        # print key, string in key
        #   find key that has string inside
        if string in key:
            _indx = key.find(string)
            #   new key - with removed string
            _key = key[_indx+len(string)::].strip()
            extracted_dictonary[_key] = dictionary[key]
    # print "output =", extracted_dictonary
    return extracted_dictonary


if __name__ == "__main__":
    d = {'contact_model.L_2':(3,4),
         'b':(1,2),
         'contact_model.K':(5,5),
         'd':(3,3)}

    print d

    condition = "contact_model."

    print extract_from_dictionary_by_string_in_key(d, condition)