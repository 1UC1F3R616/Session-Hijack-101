education = open('categories/Education.txt', 'r')
entertainment = open('categories/Entertainment.txt', 'r')
malicious = open('categories/Malicious.txt', 'r')
others = open('categories/Others.txt', 'r')
shopping = open('categories/Shopping.txt', 'r')
social = open('categories/SocialNetworking.txt', 'r')
tandt = open('categories/TravelandTourism.txt', 'r')

education_read = education.read()
entertainment_read = entertainment.read()
malicious_read = malicious.read()
others_read = others.read()
shopping_read = shopping.read()
social_read = social.read()
tandt_read = tandt.read()

education.close()


all_reads = [education_read, entertainment_read, malicious_read, others_read, shopping_read, social_read, tandt_read]
all_reads_name = ['education_read', 'entertainment_read', 'malicious_read', 'others_read', 'shopping_read', 'social_read', 'tandt_read']



import re

regex = r"[a-zA-Z0-9-]*\.(museum|travel|govuk|ltduk|moduk|netuk|nhsuk|orguk|plcuk|schuk|store|acuk|aero|arpa|asia|couk|coop|firm|info|jobs|meuk|mobi|name|nato|post|biz|cat|com|edu|gov|int|mil|net|nom|org|pro|tel|web|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cw|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|fx|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nt|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|ss|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zr|zw)$"

for ind, category in enumerate(all_reads):
    f = open('clean_categories/{}'.format(str(all_reads_name[ind])), 'w')
    
    test_str = category

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        f.write(match.group())
        f.write('\n')

    f.close()