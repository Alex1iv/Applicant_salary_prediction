# Анализ вакансий Headhunter /  Headhunter users profiles analysis
---

## Content

| **English**                                             |  **Russian**                                      |                         
| :------------------------------------------------------ | :------------------------------------------------ |
| [1. Project description](README.md#Project-description) | [1. Описание проекта](README.md#Описание-проекта) |
| [2. Data](README.md#Data)                               | [2. База данных](README.md#База-данных)           |
| [3. Inferences](README.md#Inferences)                   | [3. Выводы](README.md#Выводы)                     |
| [4. Project file](https://github.com/Alex1iv/sf_data_sci/blob/main/2.%20Recruitment_platform_user_profiles_EDA/Project_en.ipynb) | [4. Файл проекта](https://github.com/Alex1iv/sf_data_sci/blob/main/2.%20Recruitment_platform_user_profiles_EDA/Project_ru.ipynb) |

---


### Project description

HeadHunter.ru is a leading web recruitment platform in Russia and across former soviet countries. It stores multiple information about candidates and derives insights from it for offering best match for its clients (e.g. companies or enterpreneurs). Due to some reasons candidates omit to enter important information, for instance a desired salary amount.

The company manager decided to create a model, which predicts the candidate salary using information which he actually did enter and also using expectations from candidates with similar profiles.

The assignment can be logically subdivided into 4 parts:
- structural analysis of the db;
- data structuring;
- exploratory data analysis;
- data cleaning from duplicated or missed values.


The result is presented in a [jupyter-notebook](https://github.com/Alex1iv/sf_data_sci/blob/main/2.%20Recruitment_platform_user_profiles_EDA/Project_en.ipynb).

:arrow_up:[ to content](README.md#Content)


### Data
Due to large size of the data base of 61 Mb, which exceeding the GitHub' s filesize limit of 25 mb, data is stored at [Google Drive](https://drive.google.com/file/d/1LpReiJ8hQJHbGBiv1Vsp2WDYdO2qaRtA/view?usp=share_link). It was added, however, a possibility to download the archive automatically.

:arrow_up:[ to content](README.md#Content)


### Inferences
- the database was successfully cleaned from duplicated inputs and missed values.
- original database contained features, which combining heterogeneous candidates information. Since the data structure is difficult to study, it was structurized in the cleaned database. Meanwhile, the number of features in the cleaned database has increased in 2.25 times by comparisson with that of the original database.

:arrow_up:[ to content](README.md#Content)


---

### Описание проекта
Предположим, компания HeadHunter решила построить модель, которая бы автоматически определяла примерный уровень заработной платы соискателя, исходя из введённой им информации о себе. Для работы необходимо подготовить имеющуюся базу данных соискателей. 

Анализ структурно подразделяется на 4 блока:
- базовый анализ структуры данных;
-- выявление пропусков 
- преобразование данных в удобную для чтения структуру;
- разведывательный анализ;
- очистка данных.

Результат представлен в шаблоне [jupyter-ноутбука](https://github.com/Alex1iv/sf_data_sci/blob/main/2.%20Recruitment_platform_user_profiles_EDA/Project_ru.ipynb).

### База данных
Размер используемой в данном проекте базы данных составляет 61 МБ, что превышает установленны GitHub предел для загружаемых файлов в 25 мб.  Скачать базу данных можно по [ссылке на Google Drive](https://drive.google.com/file/d/1LpReiJ8hQJHbGBiv1Vsp2WDYdO2qaRtA/view?usp=share_link).

### Выводы
- база данных соискателей очищена от дублирующихся и нулевых значений.
- исходная база данных содержала признаки, объединяющие в строках разнородную информацию о соискателях. Поскольку с неоднородными строковыми данными трудно работать, они были извлечены в очищенную базу данных и распределены по нескольким признакам в удобном для дальнейшего анализа формате. Однако, это повлияло на увеличение размерности очищенной базы данных по сравнению с исходной.

:arrow_up:[ к оглавлению](README.md#Content)