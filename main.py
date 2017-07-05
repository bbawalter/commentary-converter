import re
import csv
from tkinter import *
#from fileDialog import askopenfilename
from tkinter.filedialog import askopenfilename
import os


home = os.path.expanduser('~/CorpusCoranicum/Kommentare')
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
text = askopenfilename(initialdir=home) # show an "Open" dialog box and return the path to the selected file
with open(text, 'r') as myfile:
    text_data = myfile.read()

surah = int(input("Nummer der aktuellen Sure: "))
dict_of_surah = csv.DictReader(open('hilfsmittel/max_suren_verse.csv'))
surah_dict = dict()
for row in dict_of_surah:
    surah_dict[row['Surah']] = row['Verse']



# this method removes the colour black (#000000) from formatting-tags for the sake of readability. if there is something like "italic" or "bold" (match.group(1), this should not be removed
def remove_black_in_hi(match):
    valid_format = match.group(1)
    if valid_format:
        return r'''<hi rend="%s">%s</hi>'''% (valid_format, match.group(2))
    else:
        return match.group(2)


def remove_black_in_p(match):
    if match.group(1):
        return r'''<p rend="%s"> ''' % (match.group(1))
    else:
        return r'''<p> '''

def remove_anchors(match):
    return r'''%s''' % match.group(2)


def replace_tuk(match):
    return '''<ref target="#TUK%s"> TUK, Nr. %s </ref>''' % (match.group(4).zfill(4), match.group(4).zfill(4))


def replace_surah_and_verse(match):
    # group1 = match.group(1)
    group2_v_or_q = match.group(2)
    group3 = match.group(3)
    group4 = match.group(4)
    group5 = match.group(5)
    # group6 = match.group(6)
    group7_to_verse = match.group(7)
    group8_f_or_ff = match.group(8)

    working_surah = str(surah).zfill(3)

    print()

    if group2_v_or_q in ('V', 'V.', 'Vers', 'Verse'):
        if not group7_to_verse:
            # single verse but with more than one following, this is bad form and should not be used by authors
            if group8_f_or_ff == "ff":
                three_up_due_to_ff = str(min(int(group5) + 3, int(surah_dict[group5])))
                return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"> V. %sff </q>''' % (
                    working_surah, group5.zfill(3), working_surah, three_up_due_to_ff.zfill(3), group5)


            # single verse with following verse --> f
            elif group8_f_or_ff == "f":
                one_up_due_to_f = str(int(group5) + 1)
                return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"> V. %sf </q>''' % (
                    working_surah, group5.zfill(3), working_surah, one_up_due_to_f.zfill(3), group5)

            # single verse, no f, no ff
            else:
                return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"> V. %s </q>''' % (
                    working_surah, group5.zfill(3), working_surah, group5.zfill(3), group5)

        else:
            return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"  >V. %s-%s </q>''' % (
                working_surah, group5.zfill(3), working_surah, group7_to_verse.zfill(3), group5, group7_to_verse)

    elif group2_v_or_q in ('Q'):
        # like Q 23
        if group3 == '':
            last_verse = surah_dict[group5]
            return (r'''<q type="koran" versstart="%s:000" versend="%s:%s"> Q %s </q>''' % (
                group5.zfill(3), group5.zfill(3), last_verse.zfill(3), group5))



        # single verse in other surah, like Q 23:42
        elif not group7_to_verse:
            return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"> Q %s:%s </q>''' % (
                group4.zfill(3), group5.zfill(3), group4.zfill(3), group5.zfill(3), group4, group5)

        # verse - verse in other surah, like Q 23:23-42
        else:
            return r'''<q type="koran" versstart="%s:%s" versend="%s:%s"> Q %s:%s-%s </q>''' % (
                group4.zfill(3), group5.zfill(3), group4.zfill(3), group7_to_verse.zfill(3), group4, group5,
                group7_to_verse)

    else:
        return ""


def main():
    test_string = text_data
    # test_string = '''    Q 1  Q 2 Q 34    Lot ist Protagonist auch einer der
                # Erzählungen in Q 15, in der er sich wie in Q 51 durch Gottergebenheit auszeichnet.'''

    # versfinder = re.compile(r'''(Vers|V\.) (\d+)(-(\d+)|)(f*|)''')
    # surenfinder = re.compile(r'''Q (\d+):(\d+)(-(\d+)|)(f*|)''')
    # https://regex101.com/r/HvZwFi/2
    # https://regex101.com/r/HvZwFi/4
    # colorblack_tag = re.compile(r'''<p rend=\"color\(#000000\)(\w*?)\">''')
    # highlight_finder = re.compile(r'''<hi rend=\"color\(#000000\)(\w*?)\">(.*?)</hi>''')
    # anchor_finder = re.compile(r'''(<anchor type=\"bookmark-start\".*?\"/>(.*?)<ptr target=\".*?\" type=\"bookmark-end\"/>)''')
    allesfinder = re.compile(r'''((Vers|Verse|V\.|Q)\s((\d+):|)(\d+))(-(\d+)|)(f*| )''')
    tukfinder = re.compile(r'''(TUK)(|,|:) (Nr. |Nummer |)(\d+)''')  # <ref target="#TUK1262">TUK, Nr. 1262</ref>

    # here the methods that transform he text are called
    # 1) black from hi, black from p, removing anchors, tagging of surah ands verses, tagging of tags
    # removed_black_from_hi = re.sub(highlight_finder, remove_black_in_hi, test_string)
    # removed_black_from_p = re.sub(colorblack_tag, remove_black_in_p, removed_black_from_hi)
    # no_anchors_in_text = re.sub(anchor_finder, remove_anchors, removed_black_from_p)
    surahs_and_verses_tagged = re.sub(allesfinder, replace_surah_and_verse, test_string)
    tuk_tagged = re.sub(tukfinder, replace_tuk, surahs_and_verses_tagged)
    print(tuk_tagged)
    
main()

