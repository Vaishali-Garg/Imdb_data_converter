# Imdb_data_converter

To convert the Imdb .list files to comma separated files(.csv)

### Step 1

Download the [Imdb data] (http://www.imdb.com/interfaces)

### Step 2
Unzip the imdb files.

### Step 3

Execute the converter script.

```
python3 imdb.py -d <directory-with-imdb-files> -a
```

The converter currently supports following files:
  - actors.list
  - costume-designers.list
  - actresses.list
  - certificates.list
  - cinematographers.list
  - composers.list
  - countries.list
  - directors.list
  - distributors.list
  - editors.list
  - languages.list
  - locations.list
  - movies.list
  - producers.list
  - production-companies.list
  - production-designers.list
  - ratings.list
  - release-dates.list
  - sound-mix.list
  - special-effects-companies.list
  - technical.list
  - writers.list
  - Genres.list

### Step 4

These csv files can be used to make dataframe using the following command:

```python
import pandas as pd

dfactors = pd.read_csv('actors.csv', sep = ',', encoding = 'ISO-8859-1',  error_bad_lines=False, keep_default_na=False, na_values=[''])
```

### Note
The current regex skips over some of the lines in the .list file. Here is the difference in line count:

```
bash$ for i in *.csv; do fname=`echo $i | cut -d'.' -f1`; lcount=`wc -l ${fname}.list`; ccount=`wc -l ${fname}.csv`; echo "$fname: $lcount - $ccount"; done
actors:  18988679 actors.list -  16481336 actors.csv
actresses:  11190131 actresses.list -  9810371 actresses.csv
certificates:   632458 certificates.list -   567829 certificates.csv
cinematographers:  1507632 cinematographers.list -  1237458 cinematographers.csv
composers:  1258767 composers.list -  1060267 composers.csv
costume-designers:   424631 costume-designers.list -   368472 costume-designers.csv
countries:  1747665 countries.list -  1716221 countries.csv
directors:  2821435 directors.list -  2357929 directors.csv
distributors:  1717920 distributors.list -  1496595 distributors.csv
editors:  1913515 editors.list -  1613610 editors.csv
language:  1726203 language.list -  1706164 language.csv
locations:   901125 locations.list -   813789 locations.csv
movies:  3663934 movies.list -  3562922 movies.csv
producers:  6819416 producers.list -  5891022 producers.csv
production-companies:  2284839 production-companies.list -  1858981 production-companies.csv
production-designers:   497138 production-designers.list -   424240 production-designers.csv
ratings:   667684 ratings.list -   654807 ratings.csv
release-dates:  4243932 release-dates.list -  3683960 release-dates.csv
sound-mix:   597308 sound-mix.list -   585684 sound-mix.csv
special-effects-companies:    71248 special-effects-companies.list -    42744 special-effects-companies.csv
technical:  1717554 technical.list -  1675199 technical.csv
writers:  4462728 writers.list -  3804718 writers.csv
genres: 2183747 genres.list - 2135510 genres.csv
```