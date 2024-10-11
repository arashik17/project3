{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4278ba7d",
   "metadata": {
    "papermill": {
     "duration": 0.063684,
     "end_time": "2024-10-11T19:09:46.829669",
     "exception": false,
     "start_time": "2024-10-11T19:09:46.765985",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **The Question that started this:**\n",
    "I wonder how many pets are being adopted right now? (Jan 2022, COVID Times)\n",
    "How many Intakes have happy Outcomes?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d3c3160",
   "metadata": {
    "papermill": {
     "duration": 0.064314,
     "end_time": "2024-10-11T19:09:46.957085",
     "exception": false,
     "start_time": "2024-10-11T19:09:46.892771",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### I imported a bunch of python packages before looking at the data. Some packages were added later as I tried other exploration routes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d3e0c910",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:09:47.094860Z",
     "iopub.status.busy": "2024-10-11T19:09:47.090622Z",
     "iopub.status.idle": "2024-10-11T19:09:49.174852Z",
     "shell.execute_reply": "2024-10-11T19:09:49.173720Z",
     "shell.execute_reply.started": "2022-12-16T15:18:41.694496Z"
    },
    "papermill": {
     "duration": 2.157092,
     "end_time": "2024-10-11T19:09:49.175094",
     "exception": false,
     "start_time": "2024-10-11T19:09:47.018002",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import matplotlib.dates as mdates\n",
    "from datetime import datetime\n",
    "from datetime import date\n",
    "import plotly.express as px\n",
    "import folium"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d17d17a3",
   "metadata": {
    "papermill": {
     "duration": 0.061283,
     "end_time": "2024-10-11T19:09:49.297600",
     "exception": false,
     "start_time": "2024-10-11T19:09:49.236317",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Then I imported shelter data I found, which ranged from Sonoma County to Austin County, TX"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9fa5f288",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:09:49.434103Z",
     "iopub.status.busy": "2024-10-11T19:09:49.433169Z",
     "iopub.status.idle": "2024-10-11T19:09:52.177992Z",
     "shell.execute_reply": "2024-10-11T19:09:52.177338Z",
     "shell.execute_reply.started": "2022-12-16T15:18:47.451827Z"
    },
    "papermill": {
     "duration": 2.819911,
     "end_time": "2024-10-11T19:09:52.178193",
     "exception": false,
     "start_time": "2024-10-11T19:09:49.358282",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Sonoma County, CA\n",
    "Sonoma = pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/Sonoma_County_Animal_Shelter_Intake_and_Outcome.csv')\n",
    "\n",
    "### King County, WA\n",
    "King = pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/King_CountyWALost__found__adoptable_pets.csv')\n",
    "\n",
    "### Dallas, TX\n",
    "Dallas = pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/Dallas_Animals_Inventory.csv')\n",
    "\n",
    "### Austin, TX\n",
    "Austin_Intakes = pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/Austin Animal Center Intakes.csv')\n",
    "Austin_Outcomes = pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/Austin Animal Center Outcomes.csv')\n",
    "Austin = pd.merge(Austin_Intakes, Austin_Outcomes, on='Animal ID')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b95ceb5",
   "metadata": {
    "papermill": {
     "duration": 0.061122,
     "end_time": "2024-10-11T19:09:52.299636",
     "exception": false,
     "start_time": "2024-10-11T19:09:52.238514",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "After looking at the datasets, AUSTIN has the most rows at 175034, followed by SONOMA with 22311, then DALLAS with 939 rows, and lastly, KING with 259 Rows. So, I'm going to analyze the bigger datasets, giving me a comparison between California and Texas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "88e78035",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:09:52.432062Z",
     "iopub.status.busy": "2024-10-11T19:09:52.431067Z",
     "iopub.status.idle": "2024-10-11T19:09:52.467791Z",
     "shell.execute_reply": "2024-10-11T19:09:52.468493Z",
     "shell.execute_reply.started": "2022-12-16T15:18:51.468988Z"
    },
    "papermill": {
     "duration": 0.108862,
     "end_time": "2024-10-11T19:09:52.468738",
     "exception": false,
     "start_time": "2024-10-11T19:09:52.359876",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal ID</th>\n",
       "      <th>Name_x</th>\n",
       "      <th>DateTime_x</th>\n",
       "      <th>MonthYear_x</th>\n",
       "      <th>Found Location</th>\n",
       "      <th>Intake Type</th>\n",
       "      <th>Intake Condition</th>\n",
       "      <th>Animal Type_x</th>\n",
       "      <th>Sex upon Intake</th>\n",
       "      <th>Age upon Intake</th>\n",
       "      <th>...</th>\n",
       "      <th>DateTime_y</th>\n",
       "      <th>MonthYear_y</th>\n",
       "      <th>Date of Birth</th>\n",
       "      <th>Outcome Type</th>\n",
       "      <th>Outcome Subtype</th>\n",
       "      <th>Animal Type_y</th>\n",
       "      <th>Sex upon Outcome</th>\n",
       "      <th>Age upon Outcome</th>\n",
       "      <th>Breed_y</th>\n",
       "      <th>Color_y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A786884</td>\n",
       "      <td>*Brock</td>\n",
       "      <td>01/03/2019 04:19:00 PM</td>\n",
       "      <td>01/03/2019 04:19:00 PM</td>\n",
       "      <td>2501 Magin Meadow Dr in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>...</td>\n",
       "      <td>01/08/2019 03:11:00 PM</td>\n",
       "      <td>01/08/2019 03:11:00 PM</td>\n",
       "      <td>01/03/2017</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Beagle Mix</td>\n",
       "      <td>Tricolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>A706918</td>\n",
       "      <td>Belle</td>\n",
       "      <td>07/05/2015 12:59:00 PM</td>\n",
       "      <td>07/05/2015 12:59:00 PM</td>\n",
       "      <td>9409 Bluegrass Dr in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>8 years</td>\n",
       "      <td>...</td>\n",
       "      <td>07/05/2015 03:13:00 PM</td>\n",
       "      <td>07/05/2015 03:13:00 PM</td>\n",
       "      <td>07/05/2007</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>8 years</td>\n",
       "      <td>English Springer Spaniel</td>\n",
       "      <td>White/Liver</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>A724273</td>\n",
       "      <td>Runster</td>\n",
       "      <td>04/14/2016 06:43:00 PM</td>\n",
       "      <td>04/14/2016 06:43:00 PM</td>\n",
       "      <td>2818 Palomino Trail in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>11 months</td>\n",
       "      <td>...</td>\n",
       "      <td>04/21/2016 05:17:00 PM</td>\n",
       "      <td>04/21/2016 05:17:00 PM</td>\n",
       "      <td>04/17/2015</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>1 year</td>\n",
       "      <td>Basenji Mix</td>\n",
       "      <td>Sable/White</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>A665644</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10/21/2013 07:59:00 AM</td>\n",
       "      <td>10/21/2013 07:59:00 AM</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Sick</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 weeks</td>\n",
       "      <td>...</td>\n",
       "      <td>10/21/2013 11:39:00 AM</td>\n",
       "      <td>10/21/2013 11:39:00 AM</td>\n",
       "      <td>09/21/2013</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 weeks</td>\n",
       "      <td>Domestic Shorthair Mix</td>\n",
       "      <td>Calico</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>A682524</td>\n",
       "      <td>Rio</td>\n",
       "      <td>06/29/2014 10:38:00 AM</td>\n",
       "      <td>06/29/2014 10:38:00 AM</td>\n",
       "      <td>800 Grove Blvd in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>4 years</td>\n",
       "      <td>...</td>\n",
       "      <td>07/02/2014 02:16:00 PM</td>\n",
       "      <td>07/02/2014 02:16:00 PM</td>\n",
       "      <td>06/29/2010</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Doberman Pinsch/Australian Cattle Dog</td>\n",
       "      <td>Tan/Gray</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>A743852</td>\n",
       "      <td>Odin</td>\n",
       "      <td>02/18/2017 12:46:00 PM</td>\n",
       "      <td>02/18/2017 12:46:00 PM</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Owner Surrender</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>...</td>\n",
       "      <td>02/21/2017 05:44:00 PM</td>\n",
       "      <td>02/21/2017 05:44:00 PM</td>\n",
       "      <td>02/18/2015</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Labrador Retriever Mix</td>\n",
       "      <td>Chocolate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>A635072</td>\n",
       "      <td>Beowulf</td>\n",
       "      <td>04/16/2019 09:53:00 AM</td>\n",
       "      <td>04/16/2019 09:53:00 AM</td>\n",
       "      <td>415 East Mary Street in Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>6 years</td>\n",
       "      <td>...</td>\n",
       "      <td>04/18/2019 01:45:00 PM</td>\n",
       "      <td>04/18/2019 01:45:00 PM</td>\n",
       "      <td>06/03/2012</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>6 years</td>\n",
       "      <td>Great Dane Mix</td>\n",
       "      <td>Black</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>A844350</td>\n",
       "      <td>*Ella</td>\n",
       "      <td>10/15/2021 11:40:00 AM</td>\n",
       "      <td>10/15/2021 11:40:00 AM</td>\n",
       "      <td>2112 East William Cannon Drive in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>6 months</td>\n",
       "      <td>...</td>\n",
       "      <td>10/20/2021 06:51:00 PM</td>\n",
       "      <td>10/20/2021 06:51:00 PM</td>\n",
       "      <td>04/15/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>6 months</td>\n",
       "      <td>Domestic Shorthair</td>\n",
       "      <td>Brown Tabby</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>A708452</td>\n",
       "      <td>Mumble</td>\n",
       "      <td>07/30/2015 02:37:00 PM</td>\n",
       "      <td>07/30/2015 02:37:00 PM</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>...</td>\n",
       "      <td>08/04/2015 06:17:00 PM</td>\n",
       "      <td>08/04/2015 06:17:00 PM</td>\n",
       "      <td>07/28/2013</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Labrador Retriever Mix</td>\n",
       "      <td>Black/White</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>A818975</td>\n",
       "      <td>NaN</td>\n",
       "      <td>06/18/2020 02:53:00 PM</td>\n",
       "      <td>06/18/2020 02:53:00 PM</td>\n",
       "      <td>Braker Lane And Metric in Travis (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>4 weeks</td>\n",
       "      <td>...</td>\n",
       "      <td>07/23/2020 03:54:00 PM</td>\n",
       "      <td>07/23/2020 03:54:00 PM</td>\n",
       "      <td>05/19/2020</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>Foster</td>\n",
       "      <td>Cat</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 months</td>\n",
       "      <td>Domestic Shorthair</td>\n",
       "      <td>Cream Tabby</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Animal ID   Name_x              DateTime_x             MonthYear_x  \\\n",
       "0   A786884   *Brock  01/03/2019 04:19:00 PM  01/03/2019 04:19:00 PM   \n",
       "1   A706918    Belle  07/05/2015 12:59:00 PM  07/05/2015 12:59:00 PM   \n",
       "2   A724273  Runster  04/14/2016 06:43:00 PM  04/14/2016 06:43:00 PM   \n",
       "3   A665644      NaN  10/21/2013 07:59:00 AM  10/21/2013 07:59:00 AM   \n",
       "4   A682524      Rio  06/29/2014 10:38:00 AM  06/29/2014 10:38:00 AM   \n",
       "5   A743852     Odin  02/18/2017 12:46:00 PM  02/18/2017 12:46:00 PM   \n",
       "6   A635072  Beowulf  04/16/2019 09:53:00 AM  04/16/2019 09:53:00 AM   \n",
       "7   A844350    *Ella  10/15/2021 11:40:00 AM  10/15/2021 11:40:00 AM   \n",
       "8   A708452   Mumble  07/30/2015 02:37:00 PM  07/30/2015 02:37:00 PM   \n",
       "9   A818975      NaN  06/18/2020 02:53:00 PM  06/18/2020 02:53:00 PM   \n",
       "\n",
       "                                  Found Location      Intake Type  \\\n",
       "0            2501 Magin Meadow Dr in Austin (TX)            Stray   \n",
       "1               9409 Bluegrass Dr in Austin (TX)            Stray   \n",
       "2             2818 Palomino Trail in Austin (TX)            Stray   \n",
       "3                                    Austin (TX)            Stray   \n",
       "4                  800 Grove Blvd in Austin (TX)            Stray   \n",
       "5                                    Austin (TX)  Owner Surrender   \n",
       "6            415 East Mary Street in Austin (TX)    Public Assist   \n",
       "7  2112 East William Cannon Drive in Austin (TX)            Stray   \n",
       "8                                    Austin (TX)    Public Assist   \n",
       "9          Braker Lane And Metric in Travis (TX)            Stray   \n",
       "\n",
       "  Intake Condition Animal Type_x Sex upon Intake Age upon Intake  ...  \\\n",
       "0           Normal           Dog   Neutered Male         2 years  ...   \n",
       "1           Normal           Dog   Spayed Female         8 years  ...   \n",
       "2           Normal           Dog     Intact Male       11 months  ...   \n",
       "3             Sick           Cat   Intact Female         4 weeks  ...   \n",
       "4           Normal           Dog   Neutered Male         4 years  ...   \n",
       "5           Normal           Dog   Neutered Male         2 years  ...   \n",
       "6           Normal           Dog   Neutered Male         6 years  ...   \n",
       "7           Normal           Cat   Intact Female        6 months  ...   \n",
       "8           Normal           Dog     Intact Male         2 years  ...   \n",
       "9           Normal           Cat     Intact Male         4 weeks  ...   \n",
       "\n",
       "               DateTime_y             MonthYear_y Date of Birth  \\\n",
       "0  01/08/2019 03:11:00 PM  01/08/2019 03:11:00 PM    01/03/2017   \n",
       "1  07/05/2015 03:13:00 PM  07/05/2015 03:13:00 PM    07/05/2007   \n",
       "2  04/21/2016 05:17:00 PM  04/21/2016 05:17:00 PM    04/17/2015   \n",
       "3  10/21/2013 11:39:00 AM  10/21/2013 11:39:00 AM    09/21/2013   \n",
       "4  07/02/2014 02:16:00 PM  07/02/2014 02:16:00 PM    06/29/2010   \n",
       "5  02/21/2017 05:44:00 PM  02/21/2017 05:44:00 PM    02/18/2015   \n",
       "6  04/18/2019 01:45:00 PM  04/18/2019 01:45:00 PM    06/03/2012   \n",
       "7  10/20/2021 06:51:00 PM  10/20/2021 06:51:00 PM    04/15/2021   \n",
       "8  08/04/2015 06:17:00 PM  08/04/2015 06:17:00 PM    07/28/2013   \n",
       "9  07/23/2020 03:54:00 PM  07/23/2020 03:54:00 PM    05/19/2020   \n",
       "\n",
       "      Outcome Type Outcome Subtype Animal Type_y Sex upon Outcome  \\\n",
       "0         Transfer         Partner           Dog    Neutered Male   \n",
       "1  Return to Owner             NaN           Dog    Spayed Female   \n",
       "2  Return to Owner             NaN           Dog    Neutered Male   \n",
       "3         Transfer         Partner           Cat    Intact Female   \n",
       "4  Return to Owner             NaN           Dog    Neutered Male   \n",
       "5  Return to Owner             NaN           Dog    Neutered Male   \n",
       "6  Return to Owner             NaN           Dog    Neutered Male   \n",
       "7         Adoption             NaN           Cat    Spayed Female   \n",
       "8  Return to Owner             NaN           Dog    Neutered Male   \n",
       "9         Adoption          Foster           Cat    Neutered Male   \n",
       "\n",
       "  Age upon Outcome                                Breed_y      Color_y  \n",
       "0          2 years                             Beagle Mix     Tricolor  \n",
       "1          8 years               English Springer Spaniel  White/Liver  \n",
       "2           1 year                            Basenji Mix  Sable/White  \n",
       "3          4 weeks                 Domestic Shorthair Mix       Calico  \n",
       "4          4 years  Doberman Pinsch/Australian Cattle Dog     Tan/Gray  \n",
       "5          2 years                 Labrador Retriever Mix    Chocolate  \n",
       "6          6 years                         Great Dane Mix        Black  \n",
       "7         6 months                     Domestic Shorthair  Brown Tabby  \n",
       "8          2 years                 Labrador Retriever Mix  Black/White  \n",
       "9         2 months                     Domestic Shorthair  Cream Tabby  \n",
       "\n",
       "[10 rows x 23 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "### Pull out values from columns of interest\n",
    "Austin.head(10)\n",
    "\n",
    "## Intake Condition: Normal, Sick, Injured, Pregnant, Nursing, Aged, Medical, Other, Behavior, Neonatal, Feral, Med Urgent, Space, Med Attn, Panleuk\n",
    "## Intake Type: Stray, Owner Surrender, Public Assist, Wildlife, Euthanasia Request, Abandoned\n",
    "## Animal Type_x: Dog, Cat, Bird, Livestock, Other\n",
    "## Outcome Type: Transfer, Return to Owner, Adoption, Euthanasia, Disposal, Died, Rto-Adopt, Missing, Relocate, nan\n",
    "\n",
    "## DateTime_x = Intake Date; DateTime_y = Outcome Date\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41450877",
   "metadata": {
    "papermill": {
     "duration": 0.062782,
     "end_time": "2024-10-11T19:09:52.597776",
     "exception": false,
     "start_time": "2024-10-11T19:09:52.534994",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### I then did some data cleaning and transformations on the Austin data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b16d0f5c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:09:52.752249Z",
     "iopub.status.busy": "2024-10-11T19:09:52.730531Z",
     "iopub.status.idle": "2024-10-11T19:10:33.882071Z",
     "shell.execute_reply": "2024-10-11T19:10:33.881233Z",
     "shell.execute_reply.started": "2022-12-16T15:18:57.591123Z"
    },
    "papermill": {
     "duration": 41.222173,
     "end_time": "2024-10-11T19:10:33.882281",
     "exception": false,
     "start_time": "2024-10-11T19:09:52.660108",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Replace MonthYear_x - Intake and MonthYear_y - Outcome with shortened date frame\n",
    "Austin['MonthYear_x'] = pd.to_datetime(Austin['MonthYear_x'])\n",
    "Austin['Intake Date'] = Austin['MonthYear_x'].apply(lambda x: x.strftime('%Y-%m-%d'))\n",
    "Austin['MonthYear_y'] = pd.to_datetime(Austin['MonthYear_y'])\n",
    "Austin['Outcome Date'] = Austin['MonthYear_y'].apply(lambda x: x.strftime('%Y-%m-%d'))\n",
    "Austin['Intake Month'] = Austin['MonthYear_x'].apply(lambda x: x.strftime('%B %Y'))\n",
    "Austin['Outcome Month'] = Austin['MonthYear_y'].apply(lambda x: x.strftime('%B %Y'))\n",
    "Austin['Intake Date'] = pd.to_datetime(Austin['Intake Date'])\n",
    "Austin['Outcome Date'] = pd.to_datetime(Austin['Outcome Date'])\n",
    "\n",
    "### Drop MonthYear_x and MonthYear_y\n",
    "Austin = Austin.drop(columns=['MonthYear_x', 'MonthYear_y'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9aac085a",
   "metadata": {
    "papermill": {
     "duration": 0.061547,
     "end_time": "2024-10-11T19:10:34.008031",
     "exception": false,
     "start_time": "2024-10-11T19:10:33.946484",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Asked Some Questions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3b7dc4c3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:34.183728Z",
     "iopub.status.busy": "2024-10-11T19:10:34.182822Z",
     "iopub.status.idle": "2024-10-11T19:10:35.677189Z",
     "shell.execute_reply": "2024-10-11T19:10:35.676377Z",
     "shell.execute_reply.started": "2022-12-16T15:19:29.006626Z"
    },
    "papermill": {
     "duration": 1.606858,
     "end_time": "2024-10-11T19:10:35.677384",
     "exception": false,
     "start_time": "2024-10-11T19:10:34.070526",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.8.3.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>                            <div id=\"00f48f7f-30c4-4663-8213-b337420b75b4\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"00f48f7f-30c4-4663-8213-b337420b75b4\")) {                    Plotly.newPlot(                        \"00f48f7f-30c4-4663-8213-b337420b75b4\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"x=%{x}<br>y=%{y}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"Dog\",\"Cat\",\"Other\",\"Bird\",\"Livestock\"],\"xaxis\":\"x\",\"y\":[110588,56547,7244,631,24],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"x\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"y\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"What types of Animals are Taken in?\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('00f48f7f-30c4-4663-8213-b337420b75b4');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## How many animal types are there?\n",
    "y = Austin['Animal Type_x'].value_counts()\n",
    "x = Austin['Animal Type_x'].unique()\n",
    "fig = px.bar(Austin, x=x, y=y, title='What types of Animals are Taken in?')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61cb0ee9",
   "metadata": {
    "papermill": {
     "duration": 0.063654,
     "end_time": "2024-10-11T19:10:35.807833",
     "exception": false,
     "start_time": "2024-10-11T19:10:35.744179",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c9c7dd4d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:35.986303Z",
     "iopub.status.busy": "2024-10-11T19:10:35.985444Z",
     "iopub.status.idle": "2024-10-11T19:10:36.063334Z",
     "shell.execute_reply": "2024-10-11T19:10:36.062103Z",
     "shell.execute_reply.started": "2022-12-16T15:22:11.447718Z"
    },
    "papermill": {
     "duration": 0.191164,
     "end_time": "2024-10-11T19:10:36.063543",
     "exception": false,
     "start_time": "2024-10-11T19:10:35.872379",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>                            <div id=\"9d591b92-16eb-4e34-b5f0-cfaaf4471fc2\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"9d591b92-16eb-4e34-b5f0-cfaaf4471fc2\")) {                    Plotly.newPlot(                        \"9d591b92-16eb-4e34-b5f0-cfaaf4471fc2\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"x=%{x}<br>y=%{y}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"Stray\",\"Owner Surrender\",\"Public Assist\",\"Wildlife\",\"Euthanasia Request\",\"Abandoned\"],\"xaxis\":\"x\",\"y\":[114720,41072,13004,5242,712,284],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"x\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"y\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Austin Shelters Intake Type Distribution\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('9d591b92-16eb-4e34-b5f0-cfaaf4471fc2');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y1 = Austin['Intake Type'].value_counts()\n",
    "x1 = Austin['Intake Type'].unique()\n",
    "fig1 = px.bar(Austin, x=x1, y=y1, title='Austin Shelters Intake Type Distribution')\n",
    "fig1.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2c2e017a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:36.243545Z",
     "iopub.status.busy": "2024-10-11T19:10:36.242345Z",
     "iopub.status.idle": "2024-10-11T19:10:36.322254Z",
     "shell.execute_reply": "2024-10-11T19:10:36.322846Z",
     "shell.execute_reply.started": "2022-12-16T15:22:15.677192Z"
    },
    "papermill": {
     "duration": 0.192634,
     "end_time": "2024-10-11T19:10:36.323073",
     "exception": false,
     "start_time": "2024-10-11T19:10:36.130439",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>                            <div id=\"51e642a7-28f6-45bb-b926-66e96c46d520\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"51e642a7-28f6-45bb-b926-66e96c46d520\")) {                    Plotly.newPlot(                        \"51e642a7-28f6-45bb-b926-66e96c46d520\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"x=%{x}<br>y=%{y}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"Normal\",\"Sick\",\"Injured\",\"Pregnant\",\"Nursing\",\"Aged\",\"Medical\",\"Other\",\"Behavior\",\"Neonatal\",\"Feral\",\"Med Urgent\",\"Space\",\"Med Attn\",\"Panleuk\"],\"xaxis\":\"x\",\"y\":[154562,8627,6250,4070,548,284,194,180,128,116,66,4,2,2,1],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"x\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"y\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Austin Shelters Intake Condition\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('51e642a7-28f6-45bb-b926-66e96c46d520');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## What Condition is the Animal in Upon Intake? [Intake Condition]\n",
    "\n",
    "y2 = Austin['Intake Condition'].value_counts()\n",
    "x2 = Austin['Intake Condition'].unique()\n",
    "fig1 = px.bar(Austin, x=x2, y=y2, title='Austin Shelters Intake Condition')\n",
    "fig1.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fcee8f9",
   "metadata": {
    "papermill": {
     "duration": 0.064757,
     "end_time": "2024-10-11T19:10:36.452778",
     "exception": false,
     "start_time": "2024-10-11T19:10:36.388021",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#### Created a clean data file for Austin and then changed some column dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eb33c671",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:36.595992Z",
     "iopub.status.busy": "2024-10-11T19:10:36.587649Z",
     "iopub.status.idle": "2024-10-11T19:10:39.939524Z",
     "shell.execute_reply": "2024-10-11T19:10:39.938822Z",
     "shell.execute_reply.started": "2022-12-16T15:22:23.895519Z"
    },
    "papermill": {
     "duration": 3.421327,
     "end_time": "2024-10-11T19:10:39.939713",
     "exception": false,
     "start_time": "2024-10-11T19:10:36.518386",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Austin.to_csv('Austin_Data.csv')\n",
    "Austin_Data =pd.read_csv('/kaggle/input/animal-shelter-intake-and-outcome/Austin_Data.csv')\n",
    "Austin_Data = Austin_Data.drop(columns=['Unnamed: 0'])\n",
    "Austin_Data['Intake Date'] = pd.to_datetime(Austin_Data['Intake Date'])\n",
    "Austin_Data['Outcome Date'] = pd.to_datetime(Austin_Data['Outcome Date'])\n",
    "\n",
    "Austin_Data.dtypes\n",
    "Austin_Data['Animal Type_x'] = Austin_Data['Animal Type_x'].astype('category')\n",
    "Austin_Data['Animal Type_y'] = Austin_Data['Animal Type_y'].astype('category')\n",
    "Austin_Data['Name_x'] = Austin_Data['Name_x'].astype('string')\n",
    "Austin_Data['Name_y'] = Austin_Data['Name_y'].astype('string')\n",
    "Austin_Data['Breed_x'] = Austin_Data['Breed_x'].astype('string')\n",
    "Austin_Data['Breed_y'] = Austin_Data['Breed_y'].astype('string')\n",
    "Austin_Data['Color_x'] = Austin_Data['Color_x'].astype('string')\n",
    "Austin_Data['Color_y'] = Austin_Data['Color_y'].astype('string')\n",
    "Austin_Data['DateTime_x'] = Austin_Data['DateTime_x'].astype('datetime64')\n",
    "Austin_Data['DateTime_y'] = Austin_Data['DateTime_y'].astype('datetime64')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f25a0eb",
   "metadata": {
    "papermill": {
     "duration": 0.067794,
     "end_time": "2024-10-11T19:10:40.072717",
     "exception": false,
     "start_time": "2024-10-11T19:10:40.004923",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Looked at March 2020 to Jan 2022 exclusively"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b2acb2e4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:40.216419Z",
     "iopub.status.busy": "2024-10-11T19:10:40.211629Z",
     "iopub.status.idle": "2024-10-11T19:10:40.722872Z",
     "shell.execute_reply": "2024-10-11T19:10:40.723518Z",
     "shell.execute_reply.started": "2022-12-16T15:22:29.623111Z"
    },
    "papermill": {
     "duration": 0.586183,
     "end_time": "2024-10-11T19:10:40.723735",
     "exception": false,
     "start_time": "2024-10-11T19:10:40.137552",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>                            <div id=\"d12f7856-3726-4e76-a218-4eb26dc3a40c\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"d12f7856-3726-4e76-a218-4eb26dc3a40c\")) {                    Plotly.newPlot(                        \"d12f7856-3726-4e76-a218-4eb26dc3a40c\",                        [{\"hovertemplate\":\"Animal Type_y=Bird<br>Outcome Date=%{x}<br>count=%{y}<extra></extra>\",\"legendgroup\":\"Bird\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"Bird\",\"showlegend\":true,\"x\":[\"2020-03-01T00:00:00\",\"2020-03-02T00:00:00\",\"2020-03-03T00:00:00\",\"2020-03-04T00:00:00\",\"2020-03-05T00:00:00\",\"2020-03-06T00:00:00\",\"2020-03-07T00:00:00\",\"2020-03-08T00:00:00\",\"2020-03-09T00:00:00\",\"2020-03-10T00:00:00\",\"2020-03-11T00:00:00\",\"2020-03-12T00:00:00\",\"2020-03-13T00:00:00\",\"2020-03-14T00:00:00\",\"2020-03-15T00:00:00\",\"2020-03-16T00:00:00\",\"2020-03-17T00:00:00\",\"2020-03-18T00:00:00\",\"2020-03-19T00:00:00\",\"2020-03-20T00:00:00\",\"2020-03-21T00:00:00\",\"2020-03-22T00:00:00\",\"2020-03-23T00:00:00\",\"2020-03-24T00:00:00\",\"2020-03-25T00:00:00\",\"2020-03-26T00:00:00\",\"2020-03-27T00:00:00\",\"2020-03-28T00:00:00\",\"2020-03-29T00:00:00\",\"2020-03-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-04-01T00:00:00\",\"2020-04-02T00:00:00\",\"2020-04-03T00:00:00\",\"2020-04-04T00:00:00\",\"2020-04-05T00:00:00\",\"2020-04-06T00:00:00\",\"2020-04-07T00:00:00\",\"2020-04-08T00:00:00\",\"2020-04-09T00:00:00\",\"2020-04-10T00:00:00\",\"2020-04-11T00:00:00\",\"2020-04-12T00:00:00\",\"2020-04-13T00:00:00\",\"2020-04-14T00:00:00\",\"2020-04-15T00:00:00\",\"2020-04-16T00:00:00\",\"2020-04-17T00:00:00\",\"2020-04-18T00:00:00\",\"2020-04-19T00:00:00\",\"2020-04-20T00:00:00\",\"2020-04-21T00:00:00\",\"2020-04-22T00:00:00\",\"2020-04-23T00:00:00\",\"2020-04-24T00:00:00\",\"2020-04-25T00:00:00\",\"2020-04-26T00:00:00\",\"2020-04-27T00:00:00\",\"2020-04-28T00:00:00\",\"2020-04-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-05-01T00:00:00\",\"2020-05-02T00:00:00\",\"2020-05-03T00:00:00\",\"2020-05-04T00:00:00\",\"2020-05-05T00:00:00\",\"2020-05-06T00:00:00\",\"2020-05-07T00:00:00\",\"2020-05-08T00:00:00\",\"2020-05-09T00:00:00\",\"2020-05-10T00:00:00\",\"2020-05-11T00:00:00\",\"2020-05-12T00:00:00\",\"2020-05-13T00:00:00\",\"2020-05-14T00:00:00\",\"2020-05-15T00:00:00\",\"2020-05-16T00:00:00\",\"2020-05-17T00:00:00\",\"2020-05-18T00:00:00\",\"2020-05-19T00:00:00\",\"2020-05-20T00:00:00\",\"2020-05-21T00:00:00\",\"2020-05-22T00:00:00\",\"2020-05-23T00:00:00\",\"2020-05-24T00:00:00\",\"2020-05-25T00:00:00\",\"2020-05-26T00:00:00\",\"2020-05-27T00:00:00\",\"2020-05-28T00:00:00\",\"2020-05-29T00:00:00\",\"2020-05-30T00:00:00\",\"2020-05-31T00:00:00\",\"2020-06-01T00:00:00\",\"2020-06-02T00:00:00\",\"2020-06-03T00:00:00\",\"2020-06-04T00:00:00\",\"2020-06-05T00:00:00\",\"2020-06-06T00:00:00\",\"2020-06-07T00:00:00\",\"2020-06-08T00:00:00\",\"2020-06-09T00:00:00\",\"2020-06-10T00:00:00\",\"2020-06-11T00:00:00\",\"2020-06-12T00:00:00\",\"2020-06-13T00:00:00\",\"2020-06-14T00:00:00\",\"2020-06-15T00:00:00\",\"2020-06-16T00:00:00\",\"2020-06-17T00:00:00\",\"2020-06-18T00:00:00\",\"2020-06-19T00:00:00\",\"2020-06-20T00:00:00\",\"2020-06-21T00:00:00\",\"2020-06-22T00:00:00\",\"2020-06-23T00:00:00\",\"2020-06-24T00:00:00\",\"2020-06-25T00:00:00\",\"2020-06-26T00:00:00\",\"2020-06-27T00:00:00\",\"2020-06-28T00:00:00\",\"2020-06-29T00:00:00\",\"2020-06-30T00:00:00\",\"2020-07-01T00:00:00\",\"2020-07-02T00:00:00\",\"2020-07-03T00:00:00\",\"2020-07-04T00:00:00\",\"2020-07-05T00:00:00\",\"2020-07-06T00:00:00\",\"2020-07-07T00:00:00\",\"2020-07-08T00:00:00\",\"2020-07-09T00:00:00\",\"2020-07-10T00:00:00\",\"2020-07-11T00:00:00\",\"2020-07-12T00:00:00\",\"2020-07-13T00:00:00\",\"2020-07-14T00:00:00\",\"2020-07-15T00:00:00\",\"2020-07-16T00:00:00\",\"2020-07-17T00:00:00\",\"2020-07-18T00:00:00\",\"2020-07-19T00:00:00\",\"2020-07-20T00:00:00\",\"2020-07-21T00:00:00\",\"2020-07-22T00:00:00\",\"2020-07-23T00:00:00\",\"2020-07-24T00:00:00\",\"2020-07-25T00:00:00\",\"2020-07-26T00:00:00\",\"2020-07-27T00:00:00\",\"2020-07-28T00:00:00\",\"2020-07-29T00:00:00\",\"2020-07-30T00:00:00\",\"2020-07-31T00:00:00\",\"2020-08-01T00:00:00\",\"2020-08-02T00:00:00\",\"2020-08-03T00:00:00\",\"2020-08-04T00:00:00\",\"2020-08-05T00:00:00\",\"2020-08-06T00:00:00\",\"2020-08-07T00:00:00\",\"2020-08-08T00:00:00\",\"2020-08-09T00:00:00\",\"2020-08-10T00:00:00\",\"2020-08-11T00:00:00\",\"2020-08-12T00:00:00\",\"2020-08-13T00:00:00\",\"2020-08-14T00:00:00\",\"2020-08-15T00:00:00\",\"2020-08-16T00:00:00\",\"2020-08-17T00:00:00\",\"2020-08-18T00:00:00\",\"2020-08-19T00:00:00\",\"2020-08-20T00:00:00\",\"2020-08-21T00:00:00\",\"2020-08-22T00:00:00\",\"2020-08-23T00:00:00\",\"2020-08-24T00:00:00\",\"2020-08-25T00:00:00\",\"2020-08-26T00:00:00\",\"2020-08-27T00:00:00\",\"2020-08-28T00:00:00\",\"2020-08-29T00:00:00\",\"2020-08-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-09-01T00:00:00\",\"2020-09-02T00:00:00\",\"2020-09-03T00:00:00\",\"2020-09-04T00:00:00\",\"2020-09-05T00:00:00\",\"2020-09-06T00:00:00\",\"2020-09-07T00:00:00\",\"2020-09-08T00:00:00\",\"2020-09-09T00:00:00\",\"2020-09-10T00:00:00\",\"2020-09-11T00:00:00\",\"2020-09-12T00:00:00\",\"2020-09-13T00:00:00\",\"2020-09-14T00:00:00\",\"2020-09-15T00:00:00\",\"2020-09-16T00:00:00\",\"2020-09-17T00:00:00\",\"2020-09-18T00:00:00\",\"2020-09-19T00:00:00\",\"2020-09-20T00:00:00\",\"2020-09-21T00:00:00\",\"2020-09-22T00:00:00\",\"2020-09-23T00:00:00\",\"2020-09-24T00:00:00\",\"2020-09-25T00:00:00\",\"2020-09-26T00:00:00\",\"2020-09-27T00:00:00\",\"2020-09-28T00:00:00\",\"2020-09-29T00:00:00\",\"2020-09-30T00:00:00\",\"2020-10-01T00:00:00\",\"2020-10-02T00:00:00\",\"2020-10-03T00:00:00\",\"2020-10-04T00:00:00\",\"2020-10-05T00:00:00\",\"2020-10-06T00:00:00\",\"2020-10-07T00:00:00\",\"2020-10-08T00:00:00\",\"2020-10-09T00:00:00\",\"2020-10-10T00:00:00\",\"2020-10-11T00:00:00\",\"2020-10-12T00:00:00\",\"2020-10-13T00:00:00\",\"2020-10-14T00:00:00\",\"2020-10-15T00:00:00\",\"2020-10-16T00:00:00\",\"2020-10-17T00:00:00\",\"2020-10-18T00:00:00\",\"2020-10-19T00:00:00\",\"2020-10-20T00:00:00\",\"2020-10-21T00:00:00\",\"2020-10-22T00:00:00\",\"2020-10-23T00:00:00\",\"2020-10-24T00:00:00\",\"2020-10-25T00:00:00\",\"2020-10-26T00:00:00\",\"2020-10-27T00:00:00\",\"2020-10-28T00:00:00\",\"2020-10-29T00:00:00\",\"2020-10-30T00:00:00\",\"2020-10-31T00:00:00\",\"2020-11-01T00:00:00\",\"2020-11-02T00:00:00\",\"2020-11-03T00:00:00\",\"2020-11-04T00:00:00\",\"2020-11-05T00:00:00\",\"2020-11-06T00:00:00\",\"2020-11-07T00:00:00\",\"2020-11-08T00:00:00\",\"2020-11-09T00:00:00\",\"2020-11-10T00:00:00\",\"2020-11-12T00:00:00\",\"2020-11-13T00:00:00\",\"2020-11-14T00:00:00\",\"2020-11-15T00:00:00\",\"2020-11-16T00:00:00\",\"2020-11-17T00:00:00\",\"2020-11-18T00:00:00\",\"2020-11-19T00:00:00\",\"2020-11-20T00:00:00\",\"2020-11-21T00:00:00\",\"2020-11-22T00:00:00\",\"2020-11-23T00:00:00\",\"2020-11-24T00:00:00\",\"2020-11-25T00:00:00\",\"2020-11-26T00:00:00\",\"2020-11-27T00:00:00\",\"2020-11-28T00:00:00\",\"2020-11-29T00:00:00\",\"2020-11-30T00:00:00\",\"2020-12-01T00:00:00\",\"2020-12-02T00:00:00\",\"2020-12-03T00:00:00\",\"2020-12-04T00:00:00\",\"2020-12-05T00:00:00\",\"2020-12-06T00:00:00\",\"2020-12-07T00:00:00\",\"2020-12-08T00:00:00\",\"2020-12-09T00:00:00\",\"2020-12-10T00:00:00\",\"2020-12-11T00:00:00\",\"2020-12-12T00:00:00\",\"2020-12-13T00:00:00\",\"2020-12-14T00:00:00\",\"2020-12-15T00:00:00\",\"2020-12-16T00:00:00\",\"2020-12-17T00:00:00\",\"2020-12-18T00:00:00\",\"2020-12-19T00:00:00\",\"2020-12-20T00:00:00\",\"2020-12-21T00:00:00\",\"2020-12-22T00:00:00\",\"2020-12-23T00:00:00\",\"2020-12-24T00:00:00\",\"2020-12-26T00:00:00\",\"2020-12-27T00:00:00\",\"2020-12-28T00:00:00\",\"2020-12-29T00:00:00\",\"2020-12-30T00:00:00\",\"2020-12-31T00:00:00\",\"2021-01-02T00:00:00\",\"2021-01-03T00:00:00\",\"2021-01-04T00:00:00\",\"2021-01-05T00:00:00\",\"2021-01-06T00:00:00\",\"2021-01-07T00:00:00\",\"2021-01-08T00:00:00\",\"2021-01-09T00:00:00\",\"2021-01-10T00:00:00\",\"2021-01-11T00:00:00\",\"2021-01-12T00:00:00\",\"2021-01-13T00:00:00\",\"2021-01-14T00:00:00\",\"2021-01-15T00:00:00\",\"2021-01-16T00:00:00\",\"2021-01-17T00:00:00\",\"2021-01-18T00:00:00\",\"2021-01-19T00:00:00\",\"2021-01-20T00:00:00\",\"2021-01-21T00:00:00\",\"2021-01-22T00:00:00\",\"2021-01-23T00:00:00\",\"2021-01-24T00:00:00\",\"2021-01-25T00:00:00\",\"2021-01-26T00:00:00\",\"2021-01-27T00:00:00\",\"2021-01-28T00:00:00\",\"2021-01-29T00:00:00\",\"2021-01-30T00:00:00\",\"2021-01-31T00:00:00\",\"2021-02-01T00:00:00\",\"2021-02-02T00:00:00\",\"2021-02-03T00:00:00\",\"2021-02-04T00:00:00\",\"2021-02-05T00:00:00\",\"2021-02-06T00:00:00\",\"2021-02-07T00:00:00\",\"2021-02-08T00:00:00\",\"2021-02-09T00:00:00\",\"2021-02-10T00:00:00\",\"2021-02-11T00:00:00\",\"2021-02-12T00:00:00\",\"2021-02-13T00:00:00\",\"2021-02-14T00:00:00\",\"2021-02-18T00:00:00\",\"2021-02-19T00:00:00\",\"2021-02-20T00:00:00\",\"2021-02-21T00:00:00\",\"2021-02-22T00:00:00\",\"2021-02-23T00:00:00\",\"2021-02-24T00:00:00\",\"2021-02-25T00:00:00\",\"2021-02-26T00:00:00\",\"2021-02-27T00:00:00\",\"2021-02-28T00:00:00\",\"2021-03-01T00:00:00\",\"2021-03-02T00:00:00\",\"2021-03-03T00:00:00\",\"2021-03-04T00:00:00\",\"2021-03-05T00:00:00\",\"2021-03-06T00:00:00\",\"2021-03-07T00:00:00\",\"2021-03-08T00:00:00\",\"2021-03-09T00:00:00\",\"2021-03-10T00:00:00\",\"2021-03-11T00:00:00\",\"2021-03-12T00:00:00\",\"2021-03-13T00:00:00\",\"2021-03-14T00:00:00\",\"2021-03-15T00:00:00\",\"2021-03-16T00:00:00\",\"2021-03-17T00:00:00\",\"2021-03-18T00:00:00\",\"2021-03-19T00:00:00\",\"2021-03-20T00:00:00\",\"2021-03-21T00:00:00\",\"2021-03-22T00:00:00\",\"2021-03-23T00:00:00\",\"2021-03-24T00:00:00\",\"2021-03-25T00:00:00\",\"2021-03-26T00:00:00\",\"2021-03-27T00:00:00\",\"2021-03-28T00:00:00\",\"2021-03-29T00:00:00\",\"2021-03-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-04-01T00:00:00\",\"2021-04-02T00:00:00\",\"2021-04-03T00:00:00\",\"2021-04-04T00:00:00\",\"2021-04-05T00:00:00\",\"2021-04-06T00:00:00\",\"2021-04-07T00:00:00\",\"2021-04-08T00:00:00\",\"2021-04-09T00:00:00\",\"2021-04-10T00:00:00\",\"2021-04-11T00:00:00\",\"2021-04-12T00:00:00\",\"2021-04-13T00:00:00\",\"2021-04-14T00:00:00\",\"2021-04-15T00:00:00\",\"2021-04-16T00:00:00\",\"2021-04-17T00:00:00\",\"2021-04-18T00:00:00\",\"2021-04-19T00:00:00\",\"2021-04-20T00:00:00\",\"2021-04-21T00:00:00\",\"2021-04-22T00:00:00\",\"2021-04-23T00:00:00\",\"2021-04-24T00:00:00\",\"2021-04-25T00:00:00\",\"2021-04-26T00:00:00\",\"2021-04-27T00:00:00\",\"2021-04-28T00:00:00\",\"2021-04-29T00:00:00\",\"2021-04-30T00:00:00\",\"2021-05-01T00:00:00\",\"2021-05-02T00:00:00\",\"2021-05-03T00:00:00\",\"2021-05-04T00:00:00\",\"2021-05-05T00:00:00\",\"2021-05-06T00:00:00\",\"2021-05-07T00:00:00\",\"2021-05-08T00:00:00\",\"2021-05-09T00:00:00\",\"2021-05-10T00:00:00\",\"2021-05-11T00:00:00\",\"2021-05-12T00:00:00\",\"2021-05-13T00:00:00\",\"2021-05-14T00:00:00\",\"2021-05-15T00:00:00\",\"2021-05-16T00:00:00\",\"2021-05-17T00:00:00\",\"2021-05-18T00:00:00\",\"2021-05-19T00:00:00\",\"2021-05-20T00:00:00\",\"2021-05-21T00:00:00\",\"2021-05-22T00:00:00\",\"2021-05-23T00:00:00\",\"2021-05-24T00:00:00\",\"2021-05-25T00:00:00\",\"2021-05-26T00:00:00\",\"2021-05-27T00:00:00\",\"2021-05-28T00:00:00\",\"2021-05-29T00:00:00\",\"2021-05-30T00:00:00\",\"2021-05-31T00:00:00\",\"2021-06-01T00:00:00\",\"2021-06-02T00:00:00\",\"2021-06-03T00:00:00\",\"2021-06-04T00:00:00\",\"2021-06-05T00:00:00\",\"2021-06-06T00:00:00\",\"2021-06-07T00:00:00\",\"2021-06-08T00:00:00\",\"2021-06-09T00:00:00\",\"2021-06-10T00:00:00\",\"2021-06-11T00:00:00\",\"2021-06-12T00:00:00\",\"2021-06-13T00:00:00\",\"2021-06-14T00:00:00\",\"2021-06-15T00:00:00\",\"2021-06-16T00:00:00\",\"2021-06-17T00:00:00\",\"2021-06-18T00:00:00\",\"2021-06-19T00:00:00\",\"2021-06-20T00:00:00\",\"2021-06-21T00:00:00\",\"2021-06-22T00:00:00\",\"2021-06-23T00:00:00\",\"2021-06-24T00:00:00\",\"2021-06-25T00:00:00\",\"2021-06-26T00:00:00\",\"2021-06-27T00:00:00\",\"2021-06-28T00:00:00\",\"2021-06-29T00:00:00\",\"2021-06-30T00:00:00\",\"2021-07-01T00:00:00\",\"2021-07-02T00:00:00\",\"2021-07-03T00:00:00\",\"2021-07-04T00:00:00\",\"2021-07-05T00:00:00\",\"2021-07-06T00:00:00\",\"2021-07-07T00:00:00\",\"2021-07-08T00:00:00\",\"2021-07-09T00:00:00\",\"2021-07-10T00:00:00\",\"2021-07-11T00:00:00\",\"2021-07-12T00:00:00\",\"2021-07-13T00:00:00\",\"2021-07-14T00:00:00\",\"2021-07-15T00:00:00\",\"2021-07-16T00:00:00\",\"2021-07-17T00:00:00\",\"2021-07-18T00:00:00\",\"2021-07-19T00:00:00\",\"2021-07-20T00:00:00\",\"2021-07-21T00:00:00\",\"2021-07-22T00:00:00\",\"2021-07-23T00:00:00\",\"2021-07-24T00:00:00\",\"2021-07-25T00:00:00\",\"2021-07-26T00:00:00\",\"2021-07-27T00:00:00\",\"2021-07-28T00:00:00\",\"2021-07-29T00:00:00\",\"2021-07-30T00:00:00\",\"2021-07-31T00:00:00\",\"2021-08-01T00:00:00\",\"2021-08-02T00:00:00\",\"2021-08-03T00:00:00\",\"2021-08-04T00:00:00\",\"2021-08-05T00:00:00\",\"2021-08-06T00:00:00\",\"2021-08-07T00:00:00\",\"2021-08-08T00:00:00\",\"2021-08-09T00:00:00\",\"2021-08-10T00:00:00\",\"2021-08-11T00:00:00\",\"2021-08-12T00:00:00\",\"2021-08-13T00:00:00\",\"2021-08-14T00:00:00\",\"2021-08-15T00:00:00\",\"2021-08-16T00:00:00\",\"2021-08-17T00:00:00\",\"2021-08-18T00:00:00\",\"2021-08-19T00:00:00\",\"2021-08-20T00:00:00\",\"2021-08-21T00:00:00\",\"2021-08-22T00:00:00\",\"2021-08-23T00:00:00\",\"2021-08-24T00:00:00\",\"2021-08-25T00:00:00\",\"2021-08-26T00:00:00\",\"2021-08-27T00:00:00\",\"2021-08-28T00:00:00\",\"2021-08-29T00:00:00\",\"2021-08-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-09-01T00:00:00\",\"2021-09-02T00:00:00\",\"2021-09-03T00:00:00\",\"2021-09-04T00:00:00\",\"2021-09-05T00:00:00\",\"2021-09-07T00:00:00\",\"2021-09-08T00:00:00\",\"2021-09-09T00:00:00\",\"2021-09-10T00:00:00\",\"2021-09-11T00:00:00\",\"2021-09-12T00:00:00\",\"2021-09-13T00:00:00\",\"2021-09-14T00:00:00\",\"2021-09-15T00:00:00\",\"2021-09-16T00:00:00\",\"2021-09-17T00:00:00\",\"2021-09-18T00:00:00\",\"2021-09-19T00:00:00\",\"2021-09-20T00:00:00\",\"2021-09-21T00:00:00\",\"2021-09-22T00:00:00\",\"2021-09-23T00:00:00\",\"2021-09-24T00:00:00\",\"2021-09-25T00:00:00\",\"2021-09-26T00:00:00\",\"2021-09-27T00:00:00\",\"2021-09-28T00:00:00\",\"2021-09-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-10-01T00:00:00\",\"2021-10-02T00:00:00\",\"2021-10-03T00:00:00\",\"2021-10-04T00:00:00\",\"2021-10-05T00:00:00\",\"2021-10-06T00:00:00\",\"2021-10-07T00:00:00\",\"2021-10-08T00:00:00\",\"2021-10-09T00:00:00\",\"2021-10-10T00:00:00\",\"2021-10-11T00:00:00\",\"2021-10-12T00:00:00\",\"2021-10-13T00:00:00\",\"2021-10-14T00:00:00\",\"2021-10-15T00:00:00\",\"2021-10-16T00:00:00\",\"2021-10-17T00:00:00\",\"2021-10-18T00:00:00\",\"2021-10-19T00:00:00\",\"2021-10-20T00:00:00\",\"2021-10-21T00:00:00\",\"2021-10-22T00:00:00\",\"2021-10-23T00:00:00\",\"2021-10-24T00:00:00\",\"2021-10-25T00:00:00\",\"2021-10-26T00:00:00\",\"2021-10-27T00:00:00\",\"2021-10-28T00:00:00\",\"2021-10-29T00:00:00\",\"2021-10-30T00:00:00\",\"2021-10-31T00:00:00\",\"2021-11-01T00:00:00\",\"2021-11-02T00:00:00\",\"2021-11-03T00:00:00\",\"2021-11-04T00:00:00\",\"2021-11-05T00:00:00\",\"2021-11-06T00:00:00\",\"2021-11-07T00:00:00\",\"2021-11-08T00:00:00\",\"2021-11-09T00:00:00\",\"2021-11-10T00:00:00\",\"2021-11-11T00:00:00\",\"2021-11-12T00:00:00\",\"2021-11-13T00:00:00\",\"2021-11-14T00:00:00\",\"2021-11-15T00:00:00\",\"2021-11-16T00:00:00\",\"2021-11-17T00:00:00\",\"2021-11-18T00:00:00\",\"2021-11-19T00:00:00\",\"2021-11-20T00:00:00\",\"2021-11-21T00:00:00\",\"2021-11-22T00:00:00\",\"2021-11-23T00:00:00\",\"2021-11-24T00:00:00\",\"2021-11-26T00:00:00\",\"2021-11-27T00:00:00\",\"2021-11-28T00:00:00\",\"2021-11-29T00:00:00\",\"2021-11-30T00:00:00\",\"2021-12-01T00:00:00\",\"2021-12-02T00:00:00\",\"2021-12-03T00:00:00\",\"2021-12-04T00:00:00\",\"2021-12-05T00:00:00\",\"2021-12-06T00:00:00\",\"2021-12-07T00:00:00\",\"2021-12-08T00:00:00\",\"2021-12-09T00:00:00\",\"2021-12-10T00:00:00\",\"2021-12-11T00:00:00\",\"2021-12-12T00:00:00\",\"2021-12-13T00:00:00\",\"2021-12-14T00:00:00\",\"2021-12-15T00:00:00\",\"2021-12-16T00:00:00\",\"2021-12-17T00:00:00\",\"2021-12-18T00:00:00\",\"2021-12-19T00:00:00\",\"2021-12-20T00:00:00\",\"2021-12-21T00:00:00\",\"2021-12-22T00:00:00\",\"2021-12-23T00:00:00\",\"2021-12-24T00:00:00\",\"2021-12-25T00:00:00\",\"2021-12-26T00:00:00\",\"2021-12-27T00:00:00\",\"2021-12-28T00:00:00\",\"2021-12-29T00:00:00\",\"2021-12-30T00:00:00\",\"2021-12-31T00:00:00\",\"2022-01-01T00:00:00\",\"2022-01-02T00:00:00\",\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-08T00:00:00\",\"2022-01-09T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-15T00:00:00\",\"2022-01-16T00:00:00\"],\"xaxis\":\"x\",\"y\":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,3,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,3,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"yaxis\":\"y\",\"type\":\"scattergl\"},{\"hovertemplate\":\"Animal Type_y=Cat<br>Outcome Date=%{x}<br>count=%{y}<extra></extra>\",\"legendgroup\":\"Cat\",\"line\":{\"color\":\"#EF553B\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"Cat\",\"showlegend\":true,\"x\":[\"2020-03-01T00:00:00\",\"2020-03-02T00:00:00\",\"2020-03-03T00:00:00\",\"2020-03-04T00:00:00\",\"2020-03-05T00:00:00\",\"2020-03-06T00:00:00\",\"2020-03-07T00:00:00\",\"2020-03-08T00:00:00\",\"2020-03-09T00:00:00\",\"2020-03-10T00:00:00\",\"2020-03-11T00:00:00\",\"2020-03-12T00:00:00\",\"2020-03-13T00:00:00\",\"2020-03-14T00:00:00\",\"2020-03-15T00:00:00\",\"2020-03-16T00:00:00\",\"2020-03-17T00:00:00\",\"2020-03-18T00:00:00\",\"2020-03-19T00:00:00\",\"2020-03-20T00:00:00\",\"2020-03-21T00:00:00\",\"2020-03-22T00:00:00\",\"2020-03-23T00:00:00\",\"2020-03-24T00:00:00\",\"2020-03-25T00:00:00\",\"2020-03-26T00:00:00\",\"2020-03-27T00:00:00\",\"2020-03-28T00:00:00\",\"2020-03-29T00:00:00\",\"2020-03-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-04-01T00:00:00\",\"2020-04-02T00:00:00\",\"2020-04-03T00:00:00\",\"2020-04-04T00:00:00\",\"2020-04-05T00:00:00\",\"2020-04-06T00:00:00\",\"2020-04-07T00:00:00\",\"2020-04-08T00:00:00\",\"2020-04-09T00:00:00\",\"2020-04-10T00:00:00\",\"2020-04-11T00:00:00\",\"2020-04-12T00:00:00\",\"2020-04-13T00:00:00\",\"2020-04-14T00:00:00\",\"2020-04-15T00:00:00\",\"2020-04-16T00:00:00\",\"2020-04-17T00:00:00\",\"2020-04-18T00:00:00\",\"2020-04-19T00:00:00\",\"2020-04-20T00:00:00\",\"2020-04-21T00:00:00\",\"2020-04-22T00:00:00\",\"2020-04-23T00:00:00\",\"2020-04-24T00:00:00\",\"2020-04-25T00:00:00\",\"2020-04-26T00:00:00\",\"2020-04-27T00:00:00\",\"2020-04-28T00:00:00\",\"2020-04-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-05-01T00:00:00\",\"2020-05-02T00:00:00\",\"2020-05-03T00:00:00\",\"2020-05-04T00:00:00\",\"2020-05-05T00:00:00\",\"2020-05-06T00:00:00\",\"2020-05-07T00:00:00\",\"2020-05-08T00:00:00\",\"2020-05-09T00:00:00\",\"2020-05-10T00:00:00\",\"2020-05-11T00:00:00\",\"2020-05-12T00:00:00\",\"2020-05-13T00:00:00\",\"2020-05-14T00:00:00\",\"2020-05-15T00:00:00\",\"2020-05-16T00:00:00\",\"2020-05-17T00:00:00\",\"2020-05-18T00:00:00\",\"2020-05-19T00:00:00\",\"2020-05-20T00:00:00\",\"2020-05-21T00:00:00\",\"2020-05-22T00:00:00\",\"2020-05-23T00:00:00\",\"2020-05-24T00:00:00\",\"2020-05-25T00:00:00\",\"2020-05-26T00:00:00\",\"2020-05-27T00:00:00\",\"2020-05-28T00:00:00\",\"2020-05-29T00:00:00\",\"2020-05-30T00:00:00\",\"2020-05-31T00:00:00\",\"2020-06-01T00:00:00\",\"2020-06-02T00:00:00\",\"2020-06-03T00:00:00\",\"2020-06-04T00:00:00\",\"2020-06-05T00:00:00\",\"2020-06-06T00:00:00\",\"2020-06-07T00:00:00\",\"2020-06-08T00:00:00\",\"2020-06-09T00:00:00\",\"2020-06-10T00:00:00\",\"2020-06-11T00:00:00\",\"2020-06-12T00:00:00\",\"2020-06-13T00:00:00\",\"2020-06-14T00:00:00\",\"2020-06-15T00:00:00\",\"2020-06-16T00:00:00\",\"2020-06-17T00:00:00\",\"2020-06-18T00:00:00\",\"2020-06-19T00:00:00\",\"2020-06-20T00:00:00\",\"2020-06-21T00:00:00\",\"2020-06-22T00:00:00\",\"2020-06-23T00:00:00\",\"2020-06-24T00:00:00\",\"2020-06-25T00:00:00\",\"2020-06-26T00:00:00\",\"2020-06-27T00:00:00\",\"2020-06-28T00:00:00\",\"2020-06-29T00:00:00\",\"2020-06-30T00:00:00\",\"2020-07-01T00:00:00\",\"2020-07-02T00:00:00\",\"2020-07-03T00:00:00\",\"2020-07-04T00:00:00\",\"2020-07-05T00:00:00\",\"2020-07-06T00:00:00\",\"2020-07-07T00:00:00\",\"2020-07-08T00:00:00\",\"2020-07-09T00:00:00\",\"2020-07-10T00:00:00\",\"2020-07-11T00:00:00\",\"2020-07-12T00:00:00\",\"2020-07-13T00:00:00\",\"2020-07-14T00:00:00\",\"2020-07-15T00:00:00\",\"2020-07-16T00:00:00\",\"2020-07-17T00:00:00\",\"2020-07-18T00:00:00\",\"2020-07-19T00:00:00\",\"2020-07-20T00:00:00\",\"2020-07-21T00:00:00\",\"2020-07-22T00:00:00\",\"2020-07-23T00:00:00\",\"2020-07-24T00:00:00\",\"2020-07-25T00:00:00\",\"2020-07-26T00:00:00\",\"2020-07-27T00:00:00\",\"2020-07-28T00:00:00\",\"2020-07-29T00:00:00\",\"2020-07-30T00:00:00\",\"2020-07-31T00:00:00\",\"2020-08-01T00:00:00\",\"2020-08-02T00:00:00\",\"2020-08-03T00:00:00\",\"2020-08-04T00:00:00\",\"2020-08-05T00:00:00\",\"2020-08-06T00:00:00\",\"2020-08-07T00:00:00\",\"2020-08-08T00:00:00\",\"2020-08-09T00:00:00\",\"2020-08-10T00:00:00\",\"2020-08-11T00:00:00\",\"2020-08-12T00:00:00\",\"2020-08-13T00:00:00\",\"2020-08-14T00:00:00\",\"2020-08-15T00:00:00\",\"2020-08-16T00:00:00\",\"2020-08-17T00:00:00\",\"2020-08-18T00:00:00\",\"2020-08-19T00:00:00\",\"2020-08-20T00:00:00\",\"2020-08-21T00:00:00\",\"2020-08-22T00:00:00\",\"2020-08-23T00:00:00\",\"2020-08-24T00:00:00\",\"2020-08-25T00:00:00\",\"2020-08-26T00:00:00\",\"2020-08-27T00:00:00\",\"2020-08-28T00:00:00\",\"2020-08-29T00:00:00\",\"2020-08-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-09-01T00:00:00\",\"2020-09-02T00:00:00\",\"2020-09-03T00:00:00\",\"2020-09-04T00:00:00\",\"2020-09-05T00:00:00\",\"2020-09-06T00:00:00\",\"2020-09-07T00:00:00\",\"2020-09-08T00:00:00\",\"2020-09-09T00:00:00\",\"2020-09-10T00:00:00\",\"2020-09-11T00:00:00\",\"2020-09-12T00:00:00\",\"2020-09-13T00:00:00\",\"2020-09-14T00:00:00\",\"2020-09-15T00:00:00\",\"2020-09-16T00:00:00\",\"2020-09-17T00:00:00\",\"2020-09-18T00:00:00\",\"2020-09-19T00:00:00\",\"2020-09-20T00:00:00\",\"2020-09-21T00:00:00\",\"2020-09-22T00:00:00\",\"2020-09-23T00:00:00\",\"2020-09-24T00:00:00\",\"2020-09-25T00:00:00\",\"2020-09-26T00:00:00\",\"2020-09-27T00:00:00\",\"2020-09-28T00:00:00\",\"2020-09-29T00:00:00\",\"2020-09-30T00:00:00\",\"2020-10-01T00:00:00\",\"2020-10-02T00:00:00\",\"2020-10-03T00:00:00\",\"2020-10-04T00:00:00\",\"2020-10-05T00:00:00\",\"2020-10-06T00:00:00\",\"2020-10-07T00:00:00\",\"2020-10-08T00:00:00\",\"2020-10-09T00:00:00\",\"2020-10-10T00:00:00\",\"2020-10-11T00:00:00\",\"2020-10-12T00:00:00\",\"2020-10-13T00:00:00\",\"2020-10-14T00:00:00\",\"2020-10-15T00:00:00\",\"2020-10-16T00:00:00\",\"2020-10-17T00:00:00\",\"2020-10-18T00:00:00\",\"2020-10-19T00:00:00\",\"2020-10-20T00:00:00\",\"2020-10-21T00:00:00\",\"2020-10-22T00:00:00\",\"2020-10-23T00:00:00\",\"2020-10-24T00:00:00\",\"2020-10-25T00:00:00\",\"2020-10-26T00:00:00\",\"2020-10-27T00:00:00\",\"2020-10-28T00:00:00\",\"2020-10-29T00:00:00\",\"2020-10-30T00:00:00\",\"2020-10-31T00:00:00\",\"2020-11-01T00:00:00\",\"2020-11-02T00:00:00\",\"2020-11-03T00:00:00\",\"2020-11-04T00:00:00\",\"2020-11-05T00:00:00\",\"2020-11-06T00:00:00\",\"2020-11-07T00:00:00\",\"2020-11-08T00:00:00\",\"2020-11-09T00:00:00\",\"2020-11-10T00:00:00\",\"2020-11-12T00:00:00\",\"2020-11-13T00:00:00\",\"2020-11-14T00:00:00\",\"2020-11-15T00:00:00\",\"2020-11-16T00:00:00\",\"2020-11-17T00:00:00\",\"2020-11-18T00:00:00\",\"2020-11-19T00:00:00\",\"2020-11-20T00:00:00\",\"2020-11-21T00:00:00\",\"2020-11-22T00:00:00\",\"2020-11-23T00:00:00\",\"2020-11-24T00:00:00\",\"2020-11-25T00:00:00\",\"2020-11-26T00:00:00\",\"2020-11-27T00:00:00\",\"2020-11-28T00:00:00\",\"2020-11-29T00:00:00\",\"2020-11-30T00:00:00\",\"2020-12-01T00:00:00\",\"2020-12-02T00:00:00\",\"2020-12-03T00:00:00\",\"2020-12-04T00:00:00\",\"2020-12-05T00:00:00\",\"2020-12-06T00:00:00\",\"2020-12-07T00:00:00\",\"2020-12-08T00:00:00\",\"2020-12-09T00:00:00\",\"2020-12-10T00:00:00\",\"2020-12-11T00:00:00\",\"2020-12-12T00:00:00\",\"2020-12-13T00:00:00\",\"2020-12-14T00:00:00\",\"2020-12-15T00:00:00\",\"2020-12-16T00:00:00\",\"2020-12-17T00:00:00\",\"2020-12-18T00:00:00\",\"2020-12-19T00:00:00\",\"2020-12-20T00:00:00\",\"2020-12-21T00:00:00\",\"2020-12-22T00:00:00\",\"2020-12-23T00:00:00\",\"2020-12-24T00:00:00\",\"2020-12-26T00:00:00\",\"2020-12-27T00:00:00\",\"2020-12-28T00:00:00\",\"2020-12-29T00:00:00\",\"2020-12-30T00:00:00\",\"2020-12-31T00:00:00\",\"2021-01-02T00:00:00\",\"2021-01-03T00:00:00\",\"2021-01-04T00:00:00\",\"2021-01-05T00:00:00\",\"2021-01-06T00:00:00\",\"2021-01-07T00:00:00\",\"2021-01-08T00:00:00\",\"2021-01-09T00:00:00\",\"2021-01-10T00:00:00\",\"2021-01-11T00:00:00\",\"2021-01-12T00:00:00\",\"2021-01-13T00:00:00\",\"2021-01-14T00:00:00\",\"2021-01-15T00:00:00\",\"2021-01-16T00:00:00\",\"2021-01-17T00:00:00\",\"2021-01-18T00:00:00\",\"2021-01-19T00:00:00\",\"2021-01-20T00:00:00\",\"2021-01-21T00:00:00\",\"2021-01-22T00:00:00\",\"2021-01-23T00:00:00\",\"2021-01-24T00:00:00\",\"2021-01-25T00:00:00\",\"2021-01-26T00:00:00\",\"2021-01-27T00:00:00\",\"2021-01-28T00:00:00\",\"2021-01-29T00:00:00\",\"2021-01-30T00:00:00\",\"2021-01-31T00:00:00\",\"2021-02-01T00:00:00\",\"2021-02-02T00:00:00\",\"2021-02-03T00:00:00\",\"2021-02-04T00:00:00\",\"2021-02-05T00:00:00\",\"2021-02-06T00:00:00\",\"2021-02-07T00:00:00\",\"2021-02-08T00:00:00\",\"2021-02-09T00:00:00\",\"2021-02-10T00:00:00\",\"2021-02-11T00:00:00\",\"2021-02-12T00:00:00\",\"2021-02-13T00:00:00\",\"2021-02-14T00:00:00\",\"2021-02-18T00:00:00\",\"2021-02-19T00:00:00\",\"2021-02-20T00:00:00\",\"2021-02-21T00:00:00\",\"2021-02-22T00:00:00\",\"2021-02-23T00:00:00\",\"2021-02-24T00:00:00\",\"2021-02-25T00:00:00\",\"2021-02-26T00:00:00\",\"2021-02-27T00:00:00\",\"2021-02-28T00:00:00\",\"2021-03-01T00:00:00\",\"2021-03-02T00:00:00\",\"2021-03-03T00:00:00\",\"2021-03-04T00:00:00\",\"2021-03-05T00:00:00\",\"2021-03-06T00:00:00\",\"2021-03-07T00:00:00\",\"2021-03-08T00:00:00\",\"2021-03-09T00:00:00\",\"2021-03-10T00:00:00\",\"2021-03-11T00:00:00\",\"2021-03-12T00:00:00\",\"2021-03-13T00:00:00\",\"2021-03-14T00:00:00\",\"2021-03-15T00:00:00\",\"2021-03-16T00:00:00\",\"2021-03-17T00:00:00\",\"2021-03-18T00:00:00\",\"2021-03-19T00:00:00\",\"2021-03-20T00:00:00\",\"2021-03-21T00:00:00\",\"2021-03-22T00:00:00\",\"2021-03-23T00:00:00\",\"2021-03-24T00:00:00\",\"2021-03-25T00:00:00\",\"2021-03-26T00:00:00\",\"2021-03-27T00:00:00\",\"2021-03-28T00:00:00\",\"2021-03-29T00:00:00\",\"2021-03-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-04-01T00:00:00\",\"2021-04-02T00:00:00\",\"2021-04-03T00:00:00\",\"2021-04-04T00:00:00\",\"2021-04-05T00:00:00\",\"2021-04-06T00:00:00\",\"2021-04-07T00:00:00\",\"2021-04-08T00:00:00\",\"2021-04-09T00:00:00\",\"2021-04-10T00:00:00\",\"2021-04-11T00:00:00\",\"2021-04-12T00:00:00\",\"2021-04-13T00:00:00\",\"2021-04-14T00:00:00\",\"2021-04-15T00:00:00\",\"2021-04-16T00:00:00\",\"2021-04-17T00:00:00\",\"2021-04-18T00:00:00\",\"2021-04-19T00:00:00\",\"2021-04-20T00:00:00\",\"2021-04-21T00:00:00\",\"2021-04-22T00:00:00\",\"2021-04-23T00:00:00\",\"2021-04-24T00:00:00\",\"2021-04-25T00:00:00\",\"2021-04-26T00:00:00\",\"2021-04-27T00:00:00\",\"2021-04-28T00:00:00\",\"2021-04-29T00:00:00\",\"2021-04-30T00:00:00\",\"2021-05-01T00:00:00\",\"2021-05-02T00:00:00\",\"2021-05-03T00:00:00\",\"2021-05-04T00:00:00\",\"2021-05-05T00:00:00\",\"2021-05-06T00:00:00\",\"2021-05-07T00:00:00\",\"2021-05-08T00:00:00\",\"2021-05-09T00:00:00\",\"2021-05-10T00:00:00\",\"2021-05-11T00:00:00\",\"2021-05-12T00:00:00\",\"2021-05-13T00:00:00\",\"2021-05-14T00:00:00\",\"2021-05-15T00:00:00\",\"2021-05-16T00:00:00\",\"2021-05-17T00:00:00\",\"2021-05-18T00:00:00\",\"2021-05-19T00:00:00\",\"2021-05-20T00:00:00\",\"2021-05-21T00:00:00\",\"2021-05-22T00:00:00\",\"2021-05-23T00:00:00\",\"2021-05-24T00:00:00\",\"2021-05-25T00:00:00\",\"2021-05-26T00:00:00\",\"2021-05-27T00:00:00\",\"2021-05-28T00:00:00\",\"2021-05-29T00:00:00\",\"2021-05-30T00:00:00\",\"2021-05-31T00:00:00\",\"2021-06-01T00:00:00\",\"2021-06-02T00:00:00\",\"2021-06-03T00:00:00\",\"2021-06-04T00:00:00\",\"2021-06-05T00:00:00\",\"2021-06-06T00:00:00\",\"2021-06-07T00:00:00\",\"2021-06-08T00:00:00\",\"2021-06-09T00:00:00\",\"2021-06-10T00:00:00\",\"2021-06-11T00:00:00\",\"2021-06-12T00:00:00\",\"2021-06-13T00:00:00\",\"2021-06-14T00:00:00\",\"2021-06-15T00:00:00\",\"2021-06-16T00:00:00\",\"2021-06-17T00:00:00\",\"2021-06-18T00:00:00\",\"2021-06-19T00:00:00\",\"2021-06-20T00:00:00\",\"2021-06-21T00:00:00\",\"2021-06-22T00:00:00\",\"2021-06-23T00:00:00\",\"2021-06-24T00:00:00\",\"2021-06-25T00:00:00\",\"2021-06-26T00:00:00\",\"2021-06-27T00:00:00\",\"2021-06-28T00:00:00\",\"2021-06-29T00:00:00\",\"2021-06-30T00:00:00\",\"2021-07-01T00:00:00\",\"2021-07-02T00:00:00\",\"2021-07-03T00:00:00\",\"2021-07-04T00:00:00\",\"2021-07-05T00:00:00\",\"2021-07-06T00:00:00\",\"2021-07-07T00:00:00\",\"2021-07-08T00:00:00\",\"2021-07-09T00:00:00\",\"2021-07-10T00:00:00\",\"2021-07-11T00:00:00\",\"2021-07-12T00:00:00\",\"2021-07-13T00:00:00\",\"2021-07-14T00:00:00\",\"2021-07-15T00:00:00\",\"2021-07-16T00:00:00\",\"2021-07-17T00:00:00\",\"2021-07-18T00:00:00\",\"2021-07-19T00:00:00\",\"2021-07-20T00:00:00\",\"2021-07-21T00:00:00\",\"2021-07-22T00:00:00\",\"2021-07-23T00:00:00\",\"2021-07-24T00:00:00\",\"2021-07-25T00:00:00\",\"2021-07-26T00:00:00\",\"2021-07-27T00:00:00\",\"2021-07-28T00:00:00\",\"2021-07-29T00:00:00\",\"2021-07-30T00:00:00\",\"2021-07-31T00:00:00\",\"2021-08-01T00:00:00\",\"2021-08-02T00:00:00\",\"2021-08-03T00:00:00\",\"2021-08-04T00:00:00\",\"2021-08-05T00:00:00\",\"2021-08-06T00:00:00\",\"2021-08-07T00:00:00\",\"2021-08-08T00:00:00\",\"2021-08-09T00:00:00\",\"2021-08-10T00:00:00\",\"2021-08-11T00:00:00\",\"2021-08-12T00:00:00\",\"2021-08-13T00:00:00\",\"2021-08-14T00:00:00\",\"2021-08-15T00:00:00\",\"2021-08-16T00:00:00\",\"2021-08-17T00:00:00\",\"2021-08-18T00:00:00\",\"2021-08-19T00:00:00\",\"2021-08-20T00:00:00\",\"2021-08-21T00:00:00\",\"2021-08-22T00:00:00\",\"2021-08-23T00:00:00\",\"2021-08-24T00:00:00\",\"2021-08-25T00:00:00\",\"2021-08-26T00:00:00\",\"2021-08-27T00:00:00\",\"2021-08-28T00:00:00\",\"2021-08-29T00:00:00\",\"2021-08-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-09-01T00:00:00\",\"2021-09-02T00:00:00\",\"2021-09-03T00:00:00\",\"2021-09-04T00:00:00\",\"2021-09-05T00:00:00\",\"2021-09-07T00:00:00\",\"2021-09-08T00:00:00\",\"2021-09-09T00:00:00\",\"2021-09-10T00:00:00\",\"2021-09-11T00:00:00\",\"2021-09-12T00:00:00\",\"2021-09-13T00:00:00\",\"2021-09-14T00:00:00\",\"2021-09-15T00:00:00\",\"2021-09-16T00:00:00\",\"2021-09-17T00:00:00\",\"2021-09-18T00:00:00\",\"2021-09-19T00:00:00\",\"2021-09-20T00:00:00\",\"2021-09-21T00:00:00\",\"2021-09-22T00:00:00\",\"2021-09-23T00:00:00\",\"2021-09-24T00:00:00\",\"2021-09-25T00:00:00\",\"2021-09-26T00:00:00\",\"2021-09-27T00:00:00\",\"2021-09-28T00:00:00\",\"2021-09-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-10-01T00:00:00\",\"2021-10-02T00:00:00\",\"2021-10-03T00:00:00\",\"2021-10-04T00:00:00\",\"2021-10-05T00:00:00\",\"2021-10-06T00:00:00\",\"2021-10-07T00:00:00\",\"2021-10-08T00:00:00\",\"2021-10-09T00:00:00\",\"2021-10-10T00:00:00\",\"2021-10-11T00:00:00\",\"2021-10-12T00:00:00\",\"2021-10-13T00:00:00\",\"2021-10-14T00:00:00\",\"2021-10-15T00:00:00\",\"2021-10-16T00:00:00\",\"2021-10-17T00:00:00\",\"2021-10-18T00:00:00\",\"2021-10-19T00:00:00\",\"2021-10-20T00:00:00\",\"2021-10-21T00:00:00\",\"2021-10-22T00:00:00\",\"2021-10-23T00:00:00\",\"2021-10-24T00:00:00\",\"2021-10-25T00:00:00\",\"2021-10-26T00:00:00\",\"2021-10-27T00:00:00\",\"2021-10-28T00:00:00\",\"2021-10-29T00:00:00\",\"2021-10-30T00:00:00\",\"2021-10-31T00:00:00\",\"2021-11-01T00:00:00\",\"2021-11-02T00:00:00\",\"2021-11-03T00:00:00\",\"2021-11-04T00:00:00\",\"2021-11-05T00:00:00\",\"2021-11-06T00:00:00\",\"2021-11-07T00:00:00\",\"2021-11-08T00:00:00\",\"2021-11-09T00:00:00\",\"2021-11-10T00:00:00\",\"2021-11-11T00:00:00\",\"2021-11-12T00:00:00\",\"2021-11-13T00:00:00\",\"2021-11-14T00:00:00\",\"2021-11-15T00:00:00\",\"2021-11-16T00:00:00\",\"2021-11-17T00:00:00\",\"2021-11-18T00:00:00\",\"2021-11-19T00:00:00\",\"2021-11-20T00:00:00\",\"2021-11-21T00:00:00\",\"2021-11-22T00:00:00\",\"2021-11-23T00:00:00\",\"2021-11-24T00:00:00\",\"2021-11-26T00:00:00\",\"2021-11-27T00:00:00\",\"2021-11-28T00:00:00\",\"2021-11-29T00:00:00\",\"2021-11-30T00:00:00\",\"2021-12-01T00:00:00\",\"2021-12-02T00:00:00\",\"2021-12-03T00:00:00\",\"2021-12-04T00:00:00\",\"2021-12-05T00:00:00\",\"2021-12-06T00:00:00\",\"2021-12-07T00:00:00\",\"2021-12-08T00:00:00\",\"2021-12-09T00:00:00\",\"2021-12-10T00:00:00\",\"2021-12-11T00:00:00\",\"2021-12-12T00:00:00\",\"2021-12-13T00:00:00\",\"2021-12-14T00:00:00\",\"2021-12-15T00:00:00\",\"2021-12-16T00:00:00\",\"2021-12-17T00:00:00\",\"2021-12-18T00:00:00\",\"2021-12-19T00:00:00\",\"2021-12-20T00:00:00\",\"2021-12-21T00:00:00\",\"2021-12-22T00:00:00\",\"2021-12-23T00:00:00\",\"2021-12-24T00:00:00\",\"2021-12-25T00:00:00\",\"2021-12-26T00:00:00\",\"2021-12-27T00:00:00\",\"2021-12-28T00:00:00\",\"2021-12-29T00:00:00\",\"2021-12-30T00:00:00\",\"2021-12-31T00:00:00\",\"2022-01-01T00:00:00\",\"2022-01-02T00:00:00\",\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-08T00:00:00\",\"2022-01-09T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-15T00:00:00\",\"2022-01-16T00:00:00\"],\"xaxis\":\"x\",\"y\":[12,9,13,16,19,9,11,11,4,12,6,10,10,14,14,0,5,27,0,2,4,2,2,9,3,4,7,10,1,3,10,2,5,1,5,3,7,3,0,5,6,6,0,4,0,4,6,2,2,2,1,10,2,4,4,6,9,4,2,1,9,7,0,4,5,6,5,1,5,3,8,1,9,6,5,3,8,6,6,6,14,12,4,2,4,0,3,8,3,2,9,1,11,15,19,6,2,4,2,7,17,12,10,5,6,3,10,11,12,13,14,11,2,11,11,9,9,7,11,5,13,10,15,12,7,10,2,23,17,4,5,4,3,5,8,32,10,8,14,11,9,11,42,12,3,13,3,1,7,34,23,11,13,6,4,7,35,17,12,9,16,5,6,23,21,17,16,6,1,4,17,11,16,19,5,13,14,22,16,12,17,6,8,18,25,18,15,9,10,2,1,23,7,14,24,5,5,17,9,6,19,22,23,4,12,21,10,11,6,18,4,15,37,2,20,15,5,0,6,12,5,9,5,7,3,12,17,13,21,33,8,2,4,15,4,24,37,13,10,7,12,12,15,13,17,2,6,16,11,20,5,21,4,5,20,14,11,11,2,12,14,5,8,14,15,10,12,25,6,0,1,13,9,5,23,9,18,9,13,7,20,9,19,22,11,13,9,10,26,5,13,19,27,2,5,16,18,0,18,1,5,12,16,7,16,3,2,8,5,19,7,3,0,3,16,15,4,2,7,4,2,15,18,12,3,3,8,4,13,20,6,10,19,1,3,19,7,17,3,7,0,6,6,2,4,3,8,0,5,0,1,4,1,6,5,6,4,6,3,6,11,4,7,5,5,4,6,7,16,7,6,1,4,2,13,9,15,5,10,7,4,7,10,11,6,3,2,10,13,4,1,13,17,1,7,21,16,2,7,7,12,10,8,4,5,3,7,13,5,17,12,5,5,2,6,13,12,6,20,9,10,6,17,11,23,12,8,18,4,30,11,6,10,17,27,1,13,8,16,21,6,14,13,23,26,11,27,16,20,8,2,30,14,18,25,21,17,13,30,30,19,19,17,6,18,39,21,25,4,16,19,16,25,20,18,19,15,13,19,18,36,22,25,14,10,7,34,27,27,13,33,15,19,47,27,36,29,18,26,9,26,23,22,30,21,13,27,32,28,29,22,20,3,24,41,30,15,38,13,18,30,23,25,25,39,21,4,19,26,29,30,23,11,25,30,32,16,24,21,28,9,26,30,9,14,19,15,16,34,14,12,9,15,10,45,22,16,22,22,44,9,32,20,8,8,9,30,23,26,14,32,28,23,34,5,34,21,34,20,12,20,8,38,43,19,9,17,17,8,14,23,24,19,25,33,7,46,25,19,14,15,17,9,28,29,13,14,22,26,14,31,19,20,7,16,22,17,38,24,19,11,7,17,5,10,9,21,2,25,12,17,16,19,11,11,18,7,25,16,15,19,9,13,8,17,13,19,12,11,18,18,14,20,10,21,0,3,12,21,29,16,16,25,0,13,15,16,13,22,19,25,5,13,7,22,11,10,15,6],\"yaxis\":\"y\",\"type\":\"scattergl\"},{\"hovertemplate\":\"Animal Type_y=Dog<br>Outcome Date=%{x}<br>count=%{y}<extra></extra>\",\"legendgroup\":\"Dog\",\"line\":{\"color\":\"#00cc96\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"Dog\",\"showlegend\":true,\"x\":[\"2020-03-01T00:00:00\",\"2020-03-02T00:00:00\",\"2020-03-03T00:00:00\",\"2020-03-04T00:00:00\",\"2020-03-05T00:00:00\",\"2020-03-06T00:00:00\",\"2020-03-07T00:00:00\",\"2020-03-08T00:00:00\",\"2020-03-09T00:00:00\",\"2020-03-10T00:00:00\",\"2020-03-11T00:00:00\",\"2020-03-12T00:00:00\",\"2020-03-13T00:00:00\",\"2020-03-14T00:00:00\",\"2020-03-15T00:00:00\",\"2020-03-16T00:00:00\",\"2020-03-17T00:00:00\",\"2020-03-18T00:00:00\",\"2020-03-19T00:00:00\",\"2020-03-20T00:00:00\",\"2020-03-21T00:00:00\",\"2020-03-22T00:00:00\",\"2020-03-23T00:00:00\",\"2020-03-24T00:00:00\",\"2020-03-25T00:00:00\",\"2020-03-26T00:00:00\",\"2020-03-27T00:00:00\",\"2020-03-28T00:00:00\",\"2020-03-29T00:00:00\",\"2020-03-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-04-01T00:00:00\",\"2020-04-02T00:00:00\",\"2020-04-03T00:00:00\",\"2020-04-04T00:00:00\",\"2020-04-05T00:00:00\",\"2020-04-06T00:00:00\",\"2020-04-07T00:00:00\",\"2020-04-08T00:00:00\",\"2020-04-09T00:00:00\",\"2020-04-10T00:00:00\",\"2020-04-11T00:00:00\",\"2020-04-12T00:00:00\",\"2020-04-13T00:00:00\",\"2020-04-14T00:00:00\",\"2020-04-15T00:00:00\",\"2020-04-16T00:00:00\",\"2020-04-17T00:00:00\",\"2020-04-18T00:00:00\",\"2020-04-19T00:00:00\",\"2020-04-20T00:00:00\",\"2020-04-21T00:00:00\",\"2020-04-22T00:00:00\",\"2020-04-23T00:00:00\",\"2020-04-24T00:00:00\",\"2020-04-25T00:00:00\",\"2020-04-26T00:00:00\",\"2020-04-27T00:00:00\",\"2020-04-28T00:00:00\",\"2020-04-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-05-01T00:00:00\",\"2020-05-02T00:00:00\",\"2020-05-03T00:00:00\",\"2020-05-04T00:00:00\",\"2020-05-05T00:00:00\",\"2020-05-06T00:00:00\",\"2020-05-07T00:00:00\",\"2020-05-08T00:00:00\",\"2020-05-09T00:00:00\",\"2020-05-10T00:00:00\",\"2020-05-11T00:00:00\",\"2020-05-12T00:00:00\",\"2020-05-13T00:00:00\",\"2020-05-14T00:00:00\",\"2020-05-15T00:00:00\",\"2020-05-16T00:00:00\",\"2020-05-17T00:00:00\",\"2020-05-18T00:00:00\",\"2020-05-19T00:00:00\",\"2020-05-20T00:00:00\",\"2020-05-21T00:00:00\",\"2020-05-22T00:00:00\",\"2020-05-23T00:00:00\",\"2020-05-24T00:00:00\",\"2020-05-25T00:00:00\",\"2020-05-26T00:00:00\",\"2020-05-27T00:00:00\",\"2020-05-28T00:00:00\",\"2020-05-29T00:00:00\",\"2020-05-30T00:00:00\",\"2020-05-31T00:00:00\",\"2020-06-01T00:00:00\",\"2020-06-02T00:00:00\",\"2020-06-03T00:00:00\",\"2020-06-04T00:00:00\",\"2020-06-05T00:00:00\",\"2020-06-06T00:00:00\",\"2020-06-07T00:00:00\",\"2020-06-08T00:00:00\",\"2020-06-09T00:00:00\",\"2020-06-10T00:00:00\",\"2020-06-11T00:00:00\",\"2020-06-12T00:00:00\",\"2020-06-13T00:00:00\",\"2020-06-14T00:00:00\",\"2020-06-15T00:00:00\",\"2020-06-16T00:00:00\",\"2020-06-17T00:00:00\",\"2020-06-18T00:00:00\",\"2020-06-19T00:00:00\",\"2020-06-20T00:00:00\",\"2020-06-21T00:00:00\",\"2020-06-22T00:00:00\",\"2020-06-23T00:00:00\",\"2020-06-24T00:00:00\",\"2020-06-25T00:00:00\",\"2020-06-26T00:00:00\",\"2020-06-27T00:00:00\",\"2020-06-28T00:00:00\",\"2020-06-29T00:00:00\",\"2020-06-30T00:00:00\",\"2020-07-01T00:00:00\",\"2020-07-02T00:00:00\",\"2020-07-03T00:00:00\",\"2020-07-04T00:00:00\",\"2020-07-05T00:00:00\",\"2020-07-06T00:00:00\",\"2020-07-07T00:00:00\",\"2020-07-08T00:00:00\",\"2020-07-09T00:00:00\",\"2020-07-10T00:00:00\",\"2020-07-11T00:00:00\",\"2020-07-12T00:00:00\",\"2020-07-13T00:00:00\",\"2020-07-14T00:00:00\",\"2020-07-15T00:00:00\",\"2020-07-16T00:00:00\",\"2020-07-17T00:00:00\",\"2020-07-18T00:00:00\",\"2020-07-19T00:00:00\",\"2020-07-20T00:00:00\",\"2020-07-21T00:00:00\",\"2020-07-22T00:00:00\",\"2020-07-23T00:00:00\",\"2020-07-24T00:00:00\",\"2020-07-25T00:00:00\",\"2020-07-26T00:00:00\",\"2020-07-27T00:00:00\",\"2020-07-28T00:00:00\",\"2020-07-29T00:00:00\",\"2020-07-30T00:00:00\",\"2020-07-31T00:00:00\",\"2020-08-01T00:00:00\",\"2020-08-02T00:00:00\",\"2020-08-03T00:00:00\",\"2020-08-04T00:00:00\",\"2020-08-05T00:00:00\",\"2020-08-06T00:00:00\",\"2020-08-07T00:00:00\",\"2020-08-08T00:00:00\",\"2020-08-09T00:00:00\",\"2020-08-10T00:00:00\",\"2020-08-11T00:00:00\",\"2020-08-12T00:00:00\",\"2020-08-13T00:00:00\",\"2020-08-14T00:00:00\",\"2020-08-15T00:00:00\",\"2020-08-16T00:00:00\",\"2020-08-17T00:00:00\",\"2020-08-18T00:00:00\",\"2020-08-19T00:00:00\",\"2020-08-20T00:00:00\",\"2020-08-21T00:00:00\",\"2020-08-22T00:00:00\",\"2020-08-23T00:00:00\",\"2020-08-24T00:00:00\",\"2020-08-25T00:00:00\",\"2020-08-26T00:00:00\",\"2020-08-27T00:00:00\",\"2020-08-28T00:00:00\",\"2020-08-29T00:00:00\",\"2020-08-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-09-01T00:00:00\",\"2020-09-02T00:00:00\",\"2020-09-03T00:00:00\",\"2020-09-04T00:00:00\",\"2020-09-05T00:00:00\",\"2020-09-06T00:00:00\",\"2020-09-07T00:00:00\",\"2020-09-08T00:00:00\",\"2020-09-09T00:00:00\",\"2020-09-10T00:00:00\",\"2020-09-11T00:00:00\",\"2020-09-12T00:00:00\",\"2020-09-13T00:00:00\",\"2020-09-14T00:00:00\",\"2020-09-15T00:00:00\",\"2020-09-16T00:00:00\",\"2020-09-17T00:00:00\",\"2020-09-18T00:00:00\",\"2020-09-19T00:00:00\",\"2020-09-20T00:00:00\",\"2020-09-21T00:00:00\",\"2020-09-22T00:00:00\",\"2020-09-23T00:00:00\",\"2020-09-24T00:00:00\",\"2020-09-25T00:00:00\",\"2020-09-26T00:00:00\",\"2020-09-27T00:00:00\",\"2020-09-28T00:00:00\",\"2020-09-29T00:00:00\",\"2020-09-30T00:00:00\",\"2020-10-01T00:00:00\",\"2020-10-02T00:00:00\",\"2020-10-03T00:00:00\",\"2020-10-04T00:00:00\",\"2020-10-05T00:00:00\",\"2020-10-06T00:00:00\",\"2020-10-07T00:00:00\",\"2020-10-08T00:00:00\",\"2020-10-09T00:00:00\",\"2020-10-10T00:00:00\",\"2020-10-11T00:00:00\",\"2020-10-12T00:00:00\",\"2020-10-13T00:00:00\",\"2020-10-14T00:00:00\",\"2020-10-15T00:00:00\",\"2020-10-16T00:00:00\",\"2020-10-17T00:00:00\",\"2020-10-18T00:00:00\",\"2020-10-19T00:00:00\",\"2020-10-20T00:00:00\",\"2020-10-21T00:00:00\",\"2020-10-22T00:00:00\",\"2020-10-23T00:00:00\",\"2020-10-24T00:00:00\",\"2020-10-25T00:00:00\",\"2020-10-26T00:00:00\",\"2020-10-27T00:00:00\",\"2020-10-28T00:00:00\",\"2020-10-29T00:00:00\",\"2020-10-30T00:00:00\",\"2020-10-31T00:00:00\",\"2020-11-01T00:00:00\",\"2020-11-02T00:00:00\",\"2020-11-03T00:00:00\",\"2020-11-04T00:00:00\",\"2020-11-05T00:00:00\",\"2020-11-06T00:00:00\",\"2020-11-07T00:00:00\",\"2020-11-08T00:00:00\",\"2020-11-09T00:00:00\",\"2020-11-10T00:00:00\",\"2020-11-12T00:00:00\",\"2020-11-13T00:00:00\",\"2020-11-14T00:00:00\",\"2020-11-15T00:00:00\",\"2020-11-16T00:00:00\",\"2020-11-17T00:00:00\",\"2020-11-18T00:00:00\",\"2020-11-19T00:00:00\",\"2020-11-20T00:00:00\",\"2020-11-21T00:00:00\",\"2020-11-22T00:00:00\",\"2020-11-23T00:00:00\",\"2020-11-24T00:00:00\",\"2020-11-25T00:00:00\",\"2020-11-26T00:00:00\",\"2020-11-27T00:00:00\",\"2020-11-28T00:00:00\",\"2020-11-29T00:00:00\",\"2020-11-30T00:00:00\",\"2020-12-01T00:00:00\",\"2020-12-02T00:00:00\",\"2020-12-03T00:00:00\",\"2020-12-04T00:00:00\",\"2020-12-05T00:00:00\",\"2020-12-06T00:00:00\",\"2020-12-07T00:00:00\",\"2020-12-08T00:00:00\",\"2020-12-09T00:00:00\",\"2020-12-10T00:00:00\",\"2020-12-11T00:00:00\",\"2020-12-12T00:00:00\",\"2020-12-13T00:00:00\",\"2020-12-14T00:00:00\",\"2020-12-15T00:00:00\",\"2020-12-16T00:00:00\",\"2020-12-17T00:00:00\",\"2020-12-18T00:00:00\",\"2020-12-19T00:00:00\",\"2020-12-20T00:00:00\",\"2020-12-21T00:00:00\",\"2020-12-22T00:00:00\",\"2020-12-23T00:00:00\",\"2020-12-24T00:00:00\",\"2020-12-26T00:00:00\",\"2020-12-27T00:00:00\",\"2020-12-28T00:00:00\",\"2020-12-29T00:00:00\",\"2020-12-30T00:00:00\",\"2020-12-31T00:00:00\",\"2021-01-02T00:00:00\",\"2021-01-03T00:00:00\",\"2021-01-04T00:00:00\",\"2021-01-05T00:00:00\",\"2021-01-06T00:00:00\",\"2021-01-07T00:00:00\",\"2021-01-08T00:00:00\",\"2021-01-09T00:00:00\",\"2021-01-10T00:00:00\",\"2021-01-11T00:00:00\",\"2021-01-12T00:00:00\",\"2021-01-13T00:00:00\",\"2021-01-14T00:00:00\",\"2021-01-15T00:00:00\",\"2021-01-16T00:00:00\",\"2021-01-17T00:00:00\",\"2021-01-18T00:00:00\",\"2021-01-19T00:00:00\",\"2021-01-20T00:00:00\",\"2021-01-21T00:00:00\",\"2021-01-22T00:00:00\",\"2021-01-23T00:00:00\",\"2021-01-24T00:00:00\",\"2021-01-25T00:00:00\",\"2021-01-26T00:00:00\",\"2021-01-27T00:00:00\",\"2021-01-28T00:00:00\",\"2021-01-29T00:00:00\",\"2021-01-30T00:00:00\",\"2021-01-31T00:00:00\",\"2021-02-01T00:00:00\",\"2021-02-02T00:00:00\",\"2021-02-03T00:00:00\",\"2021-02-04T00:00:00\",\"2021-02-05T00:00:00\",\"2021-02-06T00:00:00\",\"2021-02-07T00:00:00\",\"2021-02-08T00:00:00\",\"2021-02-09T00:00:00\",\"2021-02-10T00:00:00\",\"2021-02-11T00:00:00\",\"2021-02-12T00:00:00\",\"2021-02-13T00:00:00\",\"2021-02-14T00:00:00\",\"2021-02-18T00:00:00\",\"2021-02-19T00:00:00\",\"2021-02-20T00:00:00\",\"2021-02-21T00:00:00\",\"2021-02-22T00:00:00\",\"2021-02-23T00:00:00\",\"2021-02-24T00:00:00\",\"2021-02-25T00:00:00\",\"2021-02-26T00:00:00\",\"2021-02-27T00:00:00\",\"2021-02-28T00:00:00\",\"2021-03-01T00:00:00\",\"2021-03-02T00:00:00\",\"2021-03-03T00:00:00\",\"2021-03-04T00:00:00\",\"2021-03-05T00:00:00\",\"2021-03-06T00:00:00\",\"2021-03-07T00:00:00\",\"2021-03-08T00:00:00\",\"2021-03-09T00:00:00\",\"2021-03-10T00:00:00\",\"2021-03-11T00:00:00\",\"2021-03-12T00:00:00\",\"2021-03-13T00:00:00\",\"2021-03-14T00:00:00\",\"2021-03-15T00:00:00\",\"2021-03-16T00:00:00\",\"2021-03-17T00:00:00\",\"2021-03-18T00:00:00\",\"2021-03-19T00:00:00\",\"2021-03-20T00:00:00\",\"2021-03-21T00:00:00\",\"2021-03-22T00:00:00\",\"2021-03-23T00:00:00\",\"2021-03-24T00:00:00\",\"2021-03-25T00:00:00\",\"2021-03-26T00:00:00\",\"2021-03-27T00:00:00\",\"2021-03-28T00:00:00\",\"2021-03-29T00:00:00\",\"2021-03-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-04-01T00:00:00\",\"2021-04-02T00:00:00\",\"2021-04-03T00:00:00\",\"2021-04-04T00:00:00\",\"2021-04-05T00:00:00\",\"2021-04-06T00:00:00\",\"2021-04-07T00:00:00\",\"2021-04-08T00:00:00\",\"2021-04-09T00:00:00\",\"2021-04-10T00:00:00\",\"2021-04-11T00:00:00\",\"2021-04-12T00:00:00\",\"2021-04-13T00:00:00\",\"2021-04-14T00:00:00\",\"2021-04-15T00:00:00\",\"2021-04-16T00:00:00\",\"2021-04-17T00:00:00\",\"2021-04-18T00:00:00\",\"2021-04-19T00:00:00\",\"2021-04-20T00:00:00\",\"2021-04-21T00:00:00\",\"2021-04-22T00:00:00\",\"2021-04-23T00:00:00\",\"2021-04-24T00:00:00\",\"2021-04-25T00:00:00\",\"2021-04-26T00:00:00\",\"2021-04-27T00:00:00\",\"2021-04-28T00:00:00\",\"2021-04-29T00:00:00\",\"2021-04-30T00:00:00\",\"2021-05-01T00:00:00\",\"2021-05-02T00:00:00\",\"2021-05-03T00:00:00\",\"2021-05-04T00:00:00\",\"2021-05-05T00:00:00\",\"2021-05-06T00:00:00\",\"2021-05-07T00:00:00\",\"2021-05-08T00:00:00\",\"2021-05-09T00:00:00\",\"2021-05-10T00:00:00\",\"2021-05-11T00:00:00\",\"2021-05-12T00:00:00\",\"2021-05-13T00:00:00\",\"2021-05-14T00:00:00\",\"2021-05-15T00:00:00\",\"2021-05-16T00:00:00\",\"2021-05-17T00:00:00\",\"2021-05-18T00:00:00\",\"2021-05-19T00:00:00\",\"2021-05-20T00:00:00\",\"2021-05-21T00:00:00\",\"2021-05-22T00:00:00\",\"2021-05-23T00:00:00\",\"2021-05-24T00:00:00\",\"2021-05-25T00:00:00\",\"2021-05-26T00:00:00\",\"2021-05-27T00:00:00\",\"2021-05-28T00:00:00\",\"2021-05-29T00:00:00\",\"2021-05-30T00:00:00\",\"2021-05-31T00:00:00\",\"2021-06-01T00:00:00\",\"2021-06-02T00:00:00\",\"2021-06-03T00:00:00\",\"2021-06-04T00:00:00\",\"2021-06-05T00:00:00\",\"2021-06-06T00:00:00\",\"2021-06-07T00:00:00\",\"2021-06-08T00:00:00\",\"2021-06-09T00:00:00\",\"2021-06-10T00:00:00\",\"2021-06-11T00:00:00\",\"2021-06-12T00:00:00\",\"2021-06-13T00:00:00\",\"2021-06-14T00:00:00\",\"2021-06-15T00:00:00\",\"2021-06-16T00:00:00\",\"2021-06-17T00:00:00\",\"2021-06-18T00:00:00\",\"2021-06-19T00:00:00\",\"2021-06-20T00:00:00\",\"2021-06-21T00:00:00\",\"2021-06-22T00:00:00\",\"2021-06-23T00:00:00\",\"2021-06-24T00:00:00\",\"2021-06-25T00:00:00\",\"2021-06-26T00:00:00\",\"2021-06-27T00:00:00\",\"2021-06-28T00:00:00\",\"2021-06-29T00:00:00\",\"2021-06-30T00:00:00\",\"2021-07-01T00:00:00\",\"2021-07-02T00:00:00\",\"2021-07-03T00:00:00\",\"2021-07-04T00:00:00\",\"2021-07-05T00:00:00\",\"2021-07-06T00:00:00\",\"2021-07-07T00:00:00\",\"2021-07-08T00:00:00\",\"2021-07-09T00:00:00\",\"2021-07-10T00:00:00\",\"2021-07-11T00:00:00\",\"2021-07-12T00:00:00\",\"2021-07-13T00:00:00\",\"2021-07-14T00:00:00\",\"2021-07-15T00:00:00\",\"2021-07-16T00:00:00\",\"2021-07-17T00:00:00\",\"2021-07-18T00:00:00\",\"2021-07-19T00:00:00\",\"2021-07-20T00:00:00\",\"2021-07-21T00:00:00\",\"2021-07-22T00:00:00\",\"2021-07-23T00:00:00\",\"2021-07-24T00:00:00\",\"2021-07-25T00:00:00\",\"2021-07-26T00:00:00\",\"2021-07-27T00:00:00\",\"2021-07-28T00:00:00\",\"2021-07-29T00:00:00\",\"2021-07-30T00:00:00\",\"2021-07-31T00:00:00\",\"2021-08-01T00:00:00\",\"2021-08-02T00:00:00\",\"2021-08-03T00:00:00\",\"2021-08-04T00:00:00\",\"2021-08-05T00:00:00\",\"2021-08-06T00:00:00\",\"2021-08-07T00:00:00\",\"2021-08-08T00:00:00\",\"2021-08-09T00:00:00\",\"2021-08-10T00:00:00\",\"2021-08-11T00:00:00\",\"2021-08-12T00:00:00\",\"2021-08-13T00:00:00\",\"2021-08-14T00:00:00\",\"2021-08-15T00:00:00\",\"2021-08-16T00:00:00\",\"2021-08-17T00:00:00\",\"2021-08-18T00:00:00\",\"2021-08-19T00:00:00\",\"2021-08-20T00:00:00\",\"2021-08-21T00:00:00\",\"2021-08-22T00:00:00\",\"2021-08-23T00:00:00\",\"2021-08-24T00:00:00\",\"2021-08-25T00:00:00\",\"2021-08-26T00:00:00\",\"2021-08-27T00:00:00\",\"2021-08-28T00:00:00\",\"2021-08-29T00:00:00\",\"2021-08-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-09-01T00:00:00\",\"2021-09-02T00:00:00\",\"2021-09-03T00:00:00\",\"2021-09-04T00:00:00\",\"2021-09-05T00:00:00\",\"2021-09-07T00:00:00\",\"2021-09-08T00:00:00\",\"2021-09-09T00:00:00\",\"2021-09-10T00:00:00\",\"2021-09-11T00:00:00\",\"2021-09-12T00:00:00\",\"2021-09-13T00:00:00\",\"2021-09-14T00:00:00\",\"2021-09-15T00:00:00\",\"2021-09-16T00:00:00\",\"2021-09-17T00:00:00\",\"2021-09-18T00:00:00\",\"2021-09-19T00:00:00\",\"2021-09-20T00:00:00\",\"2021-09-21T00:00:00\",\"2021-09-22T00:00:00\",\"2021-09-23T00:00:00\",\"2021-09-24T00:00:00\",\"2021-09-25T00:00:00\",\"2021-09-26T00:00:00\",\"2021-09-27T00:00:00\",\"2021-09-28T00:00:00\",\"2021-09-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-10-01T00:00:00\",\"2021-10-02T00:00:00\",\"2021-10-03T00:00:00\",\"2021-10-04T00:00:00\",\"2021-10-05T00:00:00\",\"2021-10-06T00:00:00\",\"2021-10-07T00:00:00\",\"2021-10-08T00:00:00\",\"2021-10-09T00:00:00\",\"2021-10-10T00:00:00\",\"2021-10-11T00:00:00\",\"2021-10-12T00:00:00\",\"2021-10-13T00:00:00\",\"2021-10-14T00:00:00\",\"2021-10-15T00:00:00\",\"2021-10-16T00:00:00\",\"2021-10-17T00:00:00\",\"2021-10-18T00:00:00\",\"2021-10-19T00:00:00\",\"2021-10-20T00:00:00\",\"2021-10-21T00:00:00\",\"2021-10-22T00:00:00\",\"2021-10-23T00:00:00\",\"2021-10-24T00:00:00\",\"2021-10-25T00:00:00\",\"2021-10-26T00:00:00\",\"2021-10-27T00:00:00\",\"2021-10-28T00:00:00\",\"2021-10-29T00:00:00\",\"2021-10-30T00:00:00\",\"2021-10-31T00:00:00\",\"2021-11-01T00:00:00\",\"2021-11-02T00:00:00\",\"2021-11-03T00:00:00\",\"2021-11-04T00:00:00\",\"2021-11-05T00:00:00\",\"2021-11-06T00:00:00\",\"2021-11-07T00:00:00\",\"2021-11-08T00:00:00\",\"2021-11-09T00:00:00\",\"2021-11-10T00:00:00\",\"2021-11-11T00:00:00\",\"2021-11-12T00:00:00\",\"2021-11-13T00:00:00\",\"2021-11-14T00:00:00\",\"2021-11-15T00:00:00\",\"2021-11-16T00:00:00\",\"2021-11-17T00:00:00\",\"2021-11-18T00:00:00\",\"2021-11-19T00:00:00\",\"2021-11-20T00:00:00\",\"2021-11-21T00:00:00\",\"2021-11-22T00:00:00\",\"2021-11-23T00:00:00\",\"2021-11-24T00:00:00\",\"2021-11-26T00:00:00\",\"2021-11-27T00:00:00\",\"2021-11-28T00:00:00\",\"2021-11-29T00:00:00\",\"2021-11-30T00:00:00\",\"2021-12-01T00:00:00\",\"2021-12-02T00:00:00\",\"2021-12-03T00:00:00\",\"2021-12-04T00:00:00\",\"2021-12-05T00:00:00\",\"2021-12-06T00:00:00\",\"2021-12-07T00:00:00\",\"2021-12-08T00:00:00\",\"2021-12-09T00:00:00\",\"2021-12-10T00:00:00\",\"2021-12-11T00:00:00\",\"2021-12-12T00:00:00\",\"2021-12-13T00:00:00\",\"2021-12-14T00:00:00\",\"2021-12-15T00:00:00\",\"2021-12-16T00:00:00\",\"2021-12-17T00:00:00\",\"2021-12-18T00:00:00\",\"2021-12-19T00:00:00\",\"2021-12-20T00:00:00\",\"2021-12-21T00:00:00\",\"2021-12-22T00:00:00\",\"2021-12-23T00:00:00\",\"2021-12-24T00:00:00\",\"2021-12-25T00:00:00\",\"2021-12-26T00:00:00\",\"2021-12-27T00:00:00\",\"2021-12-28T00:00:00\",\"2021-12-29T00:00:00\",\"2021-12-30T00:00:00\",\"2021-12-31T00:00:00\",\"2022-01-01T00:00:00\",\"2022-01-02T00:00:00\",\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-08T00:00:00\",\"2022-01-09T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-15T00:00:00\",\"2022-01-16T00:00:00\"],\"xaxis\":\"x\",\"y\":[28,52,31,45,43,43,29,34,37,45,30,45,40,49,46,25,34,16,5,12,3,9,4,40,13,11,6,15,9,2,27,19,20,6,28,11,6,24,12,11,11,8,0,16,12,19,30,2,15,5,6,27,11,5,6,4,8,6,11,14,6,10,12,2,4,14,16,21,18,9,2,4,26,16,8,11,16,10,7,14,18,4,10,3,25,0,30,29,7,9,18,6,18,24,42,10,17,10,10,28,20,26,14,13,6,9,20,24,14,10,13,11,6,23,25,10,13,17,4,14,16,23,31,12,7,8,9,10,35,10,14,9,12,11,18,30,18,12,20,16,2,22,13,16,8,8,4,6,21,32,14,14,16,19,18,10,17,19,33,13,15,2,14,39,17,16,14,4,10,20,19,23,10,9,21,4,10,28,24,14,36,14,8,13,19,13,8,9,18,5,1,32,15,20,11,34,2,60,25,13,20,18,12,9,12,38,24,22,16,33,8,22,31,14,25,10,9,10,35,36,12,21,43,16,5,4,41,18,20,23,15,3,11,34,7,18,24,13,16,18,32,20,19,23,22,4,20,21,18,16,18,16,17,22,23,34,39,19,10,18,27,12,14,15,27,11,20,34,25,2,1,16,15,21,26,19,41,45,23,4,27,35,23,19,15,11,12,24,30,17,21,27,31,5,21,20,12,0,14,5,22,13,11,14,27,15,5,17,28,21,22,8,4,21,15,19,14,35,12,16,0,21,13,20,23,23,3,9,25,30,27,20,33,6,20,24,14,31,17,20,13,12,32,9,18,20,18,1,9,10,12,8,14,21,15,14,16,21,13,13,44,12,25,9,23,10,18,17,10,10,28,41,6,24,32,13,21,16,13,8,11,26,12,18,25,20,16,32,16,22,23,36,24,12,17,17,11,17,13,7,17,18,16,13,12,34,17,11,33,27,9,21,25,8,10,25,18,14,20,31,45,12,18,22,41,26,33,39,39,20,29,17,22,22,25,31,16,36,8,27,23,12,11,18,29,17,18,23,12,14,4,28,25,29,18,38,23,30,39,24,19,15,28,16,24,26,25,40,2,22,21,49,24,29,20,45,46,6,51,36,41,37,39,29,20,2,55,30,22,17,39,17,28,18,36,36,27,25,24,32,40,22,26,18,24,48,39,38,12,28,29,20,17,45,29,26,21,58,12,12,20,24,23,17,18,37,18,22,28,25,29,24,20,31,37,29,20,35,35,34,11,27,18,22,24,28,21,27,29,22,34,17,33,20,35,22,21,43,24,52,32,33,30,22,25,31,21,16,42,51,37,20,24,15,25,43,25,18,21,53,24,14,24,24,23,16,25,19,9,40,29,26,16,42,25,15,28,36,17,20,13,14,11,60,12,10,22,51,22,20,26,22,27,1,32,59,23,36,19,16,16,52,24,17,19,20,31,4,38,12,37,21,40,23,20,26,26,41,16,26,19,47,41,8,20,18,16,37,18,21,31,44,47,42,30,1,0,15,23,18,50,19,32,4,15,40,23,26,27,71,20,17,12,21,37,19,35,17,10],\"yaxis\":\"y\",\"type\":\"scattergl\"},{\"hovertemplate\":\"Animal Type_y=Livestock<br>Outcome Date=%{x}<br>count=%{y}<extra></extra>\",\"legendgroup\":\"Livestock\",\"line\":{\"color\":\"#ab63fa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"Livestock\",\"showlegend\":true,\"x\":[\"2020-03-01T00:00:00\",\"2020-03-02T00:00:00\",\"2020-03-03T00:00:00\",\"2020-03-04T00:00:00\",\"2020-03-05T00:00:00\",\"2020-03-06T00:00:00\",\"2020-03-07T00:00:00\",\"2020-03-08T00:00:00\",\"2020-03-09T00:00:00\",\"2020-03-10T00:00:00\",\"2020-03-11T00:00:00\",\"2020-03-12T00:00:00\",\"2020-03-13T00:00:00\",\"2020-03-14T00:00:00\",\"2020-03-15T00:00:00\",\"2020-03-16T00:00:00\",\"2020-03-17T00:00:00\",\"2020-03-18T00:00:00\",\"2020-03-19T00:00:00\",\"2020-03-20T00:00:00\",\"2020-03-21T00:00:00\",\"2020-03-22T00:00:00\",\"2020-03-23T00:00:00\",\"2020-03-24T00:00:00\",\"2020-03-25T00:00:00\",\"2020-03-26T00:00:00\",\"2020-03-27T00:00:00\",\"2020-03-28T00:00:00\",\"2020-03-29T00:00:00\",\"2020-03-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-04-01T00:00:00\",\"2020-04-02T00:00:00\",\"2020-04-03T00:00:00\",\"2020-04-04T00:00:00\",\"2020-04-05T00:00:00\",\"2020-04-06T00:00:00\",\"2020-04-07T00:00:00\",\"2020-04-08T00:00:00\",\"2020-04-09T00:00:00\",\"2020-04-10T00:00:00\",\"2020-04-11T00:00:00\",\"2020-04-12T00:00:00\",\"2020-04-13T00:00:00\",\"2020-04-14T00:00:00\",\"2020-04-15T00:00:00\",\"2020-04-16T00:00:00\",\"2020-04-17T00:00:00\",\"2020-04-18T00:00:00\",\"2020-04-19T00:00:00\",\"2020-04-20T00:00:00\",\"2020-04-21T00:00:00\",\"2020-04-22T00:00:00\",\"2020-04-23T00:00:00\",\"2020-04-24T00:00:00\",\"2020-04-25T00:00:00\",\"2020-04-26T00:00:00\",\"2020-04-27T00:00:00\",\"2020-04-28T00:00:00\",\"2020-04-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-05-01T00:00:00\",\"2020-05-02T00:00:00\",\"2020-05-03T00:00:00\",\"2020-05-04T00:00:00\",\"2020-05-05T00:00:00\",\"2020-05-06T00:00:00\",\"2020-05-07T00:00:00\",\"2020-05-08T00:00:00\",\"2020-05-09T00:00:00\",\"2020-05-10T00:00:00\",\"2020-05-11T00:00:00\",\"2020-05-12T00:00:00\",\"2020-05-13T00:00:00\",\"2020-05-14T00:00:00\",\"2020-05-15T00:00:00\",\"2020-05-16T00:00:00\",\"2020-05-17T00:00:00\",\"2020-05-18T00:00:00\",\"2020-05-19T00:00:00\",\"2020-05-20T00:00:00\",\"2020-05-21T00:00:00\",\"2020-05-22T00:00:00\",\"2020-05-23T00:00:00\",\"2020-05-24T00:00:00\",\"2020-05-25T00:00:00\",\"2020-05-26T00:00:00\",\"2020-05-27T00:00:00\",\"2020-05-28T00:00:00\",\"2020-05-29T00:00:00\",\"2020-05-30T00:00:00\",\"2020-05-31T00:00:00\",\"2020-06-01T00:00:00\",\"2020-06-02T00:00:00\",\"2020-06-03T00:00:00\",\"2020-06-04T00:00:00\",\"2020-06-05T00:00:00\",\"2020-06-06T00:00:00\",\"2020-06-07T00:00:00\",\"2020-06-08T00:00:00\",\"2020-06-09T00:00:00\",\"2020-06-10T00:00:00\",\"2020-06-11T00:00:00\",\"2020-06-12T00:00:00\",\"2020-06-13T00:00:00\",\"2020-06-14T00:00:00\",\"2020-06-15T00:00:00\",\"2020-06-16T00:00:00\",\"2020-06-17T00:00:00\",\"2020-06-18T00:00:00\",\"2020-06-19T00:00:00\",\"2020-06-20T00:00:00\",\"2020-06-21T00:00:00\",\"2020-06-22T00:00:00\",\"2020-06-23T00:00:00\",\"2020-06-24T00:00:00\",\"2020-06-25T00:00:00\",\"2020-06-26T00:00:00\",\"2020-06-27T00:00:00\",\"2020-06-28T00:00:00\",\"2020-06-29T00:00:00\",\"2020-06-30T00:00:00\",\"2020-07-01T00:00:00\",\"2020-07-02T00:00:00\",\"2020-07-03T00:00:00\",\"2020-07-04T00:00:00\",\"2020-07-05T00:00:00\",\"2020-07-06T00:00:00\",\"2020-07-07T00:00:00\",\"2020-07-08T00:00:00\",\"2020-07-09T00:00:00\",\"2020-07-10T00:00:00\",\"2020-07-11T00:00:00\",\"2020-07-12T00:00:00\",\"2020-07-13T00:00:00\",\"2020-07-14T00:00:00\",\"2020-07-15T00:00:00\",\"2020-07-16T00:00:00\",\"2020-07-17T00:00:00\",\"2020-07-18T00:00:00\",\"2020-07-19T00:00:00\",\"2020-07-20T00:00:00\",\"2020-07-21T00:00:00\",\"2020-07-22T00:00:00\",\"2020-07-23T00:00:00\",\"2020-07-24T00:00:00\",\"2020-07-25T00:00:00\",\"2020-07-26T00:00:00\",\"2020-07-27T00:00:00\",\"2020-07-28T00:00:00\",\"2020-07-29T00:00:00\",\"2020-07-30T00:00:00\",\"2020-07-31T00:00:00\",\"2020-08-01T00:00:00\",\"2020-08-02T00:00:00\",\"2020-08-03T00:00:00\",\"2020-08-04T00:00:00\",\"2020-08-05T00:00:00\",\"2020-08-06T00:00:00\",\"2020-08-07T00:00:00\",\"2020-08-08T00:00:00\",\"2020-08-09T00:00:00\",\"2020-08-10T00:00:00\",\"2020-08-11T00:00:00\",\"2020-08-12T00:00:00\",\"2020-08-13T00:00:00\",\"2020-08-14T00:00:00\",\"2020-08-15T00:00:00\",\"2020-08-16T00:00:00\",\"2020-08-17T00:00:00\",\"2020-08-18T00:00:00\",\"2020-08-19T00:00:00\",\"2020-08-20T00:00:00\",\"2020-08-21T00:00:00\",\"2020-08-22T00:00:00\",\"2020-08-23T00:00:00\",\"2020-08-24T00:00:00\",\"2020-08-25T00:00:00\",\"2020-08-26T00:00:00\",\"2020-08-27T00:00:00\",\"2020-08-28T00:00:00\",\"2020-08-29T00:00:00\",\"2020-08-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-09-01T00:00:00\",\"2020-09-02T00:00:00\",\"2020-09-03T00:00:00\",\"2020-09-04T00:00:00\",\"2020-09-05T00:00:00\",\"2020-09-06T00:00:00\",\"2020-09-07T00:00:00\",\"2020-09-08T00:00:00\",\"2020-09-09T00:00:00\",\"2020-09-10T00:00:00\",\"2020-09-11T00:00:00\",\"2020-09-12T00:00:00\",\"2020-09-13T00:00:00\",\"2020-09-14T00:00:00\",\"2020-09-15T00:00:00\",\"2020-09-16T00:00:00\",\"2020-09-17T00:00:00\",\"2020-09-18T00:00:00\",\"2020-09-19T00:00:00\",\"2020-09-20T00:00:00\",\"2020-09-21T00:00:00\",\"2020-09-22T00:00:00\",\"2020-09-23T00:00:00\",\"2020-09-24T00:00:00\",\"2020-09-25T00:00:00\",\"2020-09-26T00:00:00\",\"2020-09-27T00:00:00\",\"2020-09-28T00:00:00\",\"2020-09-29T00:00:00\",\"2020-09-30T00:00:00\",\"2020-10-01T00:00:00\",\"2020-10-02T00:00:00\",\"2020-10-03T00:00:00\",\"2020-10-04T00:00:00\",\"2020-10-05T00:00:00\",\"2020-10-06T00:00:00\",\"2020-10-07T00:00:00\",\"2020-10-08T00:00:00\",\"2020-10-09T00:00:00\",\"2020-10-10T00:00:00\",\"2020-10-11T00:00:00\",\"2020-10-12T00:00:00\",\"2020-10-13T00:00:00\",\"2020-10-14T00:00:00\",\"2020-10-15T00:00:00\",\"2020-10-16T00:00:00\",\"2020-10-17T00:00:00\",\"2020-10-18T00:00:00\",\"2020-10-19T00:00:00\",\"2020-10-20T00:00:00\",\"2020-10-21T00:00:00\",\"2020-10-22T00:00:00\",\"2020-10-23T00:00:00\",\"2020-10-24T00:00:00\",\"2020-10-25T00:00:00\",\"2020-10-26T00:00:00\",\"2020-10-27T00:00:00\",\"2020-10-28T00:00:00\",\"2020-10-29T00:00:00\",\"2020-10-30T00:00:00\",\"2020-10-31T00:00:00\",\"2020-11-01T00:00:00\",\"2020-11-02T00:00:00\",\"2020-11-03T00:00:00\",\"2020-11-04T00:00:00\",\"2020-11-05T00:00:00\",\"2020-11-06T00:00:00\",\"2020-11-07T00:00:00\",\"2020-11-08T00:00:00\",\"2020-11-09T00:00:00\",\"2020-11-10T00:00:00\",\"2020-11-12T00:00:00\",\"2020-11-13T00:00:00\",\"2020-11-14T00:00:00\",\"2020-11-15T00:00:00\",\"2020-11-16T00:00:00\",\"2020-11-17T00:00:00\",\"2020-11-18T00:00:00\",\"2020-11-19T00:00:00\",\"2020-11-20T00:00:00\",\"2020-11-21T00:00:00\",\"2020-11-22T00:00:00\",\"2020-11-23T00:00:00\",\"2020-11-24T00:00:00\",\"2020-11-25T00:00:00\",\"2020-11-26T00:00:00\",\"2020-11-27T00:00:00\",\"2020-11-28T00:00:00\",\"2020-11-29T00:00:00\",\"2020-11-30T00:00:00\",\"2020-12-01T00:00:00\",\"2020-12-02T00:00:00\",\"2020-12-03T00:00:00\",\"2020-12-04T00:00:00\",\"2020-12-05T00:00:00\",\"2020-12-06T00:00:00\",\"2020-12-07T00:00:00\",\"2020-12-08T00:00:00\",\"2020-12-09T00:00:00\",\"2020-12-10T00:00:00\",\"2020-12-11T00:00:00\",\"2020-12-12T00:00:00\",\"2020-12-13T00:00:00\",\"2020-12-14T00:00:00\",\"2020-12-15T00:00:00\",\"2020-12-16T00:00:00\",\"2020-12-17T00:00:00\",\"2020-12-18T00:00:00\",\"2020-12-19T00:00:00\",\"2020-12-20T00:00:00\",\"2020-12-21T00:00:00\",\"2020-12-22T00:00:00\",\"2020-12-23T00:00:00\",\"2020-12-24T00:00:00\",\"2020-12-26T00:00:00\",\"2020-12-27T00:00:00\",\"2020-12-28T00:00:00\",\"2020-12-29T00:00:00\",\"2020-12-30T00:00:00\",\"2020-12-31T00:00:00\",\"2021-01-02T00:00:00\",\"2021-01-03T00:00:00\",\"2021-01-04T00:00:00\",\"2021-01-05T00:00:00\",\"2021-01-06T00:00:00\",\"2021-01-07T00:00:00\",\"2021-01-08T00:00:00\",\"2021-01-09T00:00:00\",\"2021-01-10T00:00:00\",\"2021-01-11T00:00:00\",\"2021-01-12T00:00:00\",\"2021-01-13T00:00:00\",\"2021-01-14T00:00:00\",\"2021-01-15T00:00:00\",\"2021-01-16T00:00:00\",\"2021-01-17T00:00:00\",\"2021-01-18T00:00:00\",\"2021-01-19T00:00:00\",\"2021-01-20T00:00:00\",\"2021-01-21T00:00:00\",\"2021-01-22T00:00:00\",\"2021-01-23T00:00:00\",\"2021-01-24T00:00:00\",\"2021-01-25T00:00:00\",\"2021-01-26T00:00:00\",\"2021-01-27T00:00:00\",\"2021-01-28T00:00:00\",\"2021-01-29T00:00:00\",\"2021-01-30T00:00:00\",\"2021-01-31T00:00:00\",\"2021-02-01T00:00:00\",\"2021-02-02T00:00:00\",\"2021-02-03T00:00:00\",\"2021-02-04T00:00:00\",\"2021-02-05T00:00:00\",\"2021-02-06T00:00:00\",\"2021-02-07T00:00:00\",\"2021-02-08T00:00:00\",\"2021-02-09T00:00:00\",\"2021-02-10T00:00:00\",\"2021-02-11T00:00:00\",\"2021-02-12T00:00:00\",\"2021-02-13T00:00:00\",\"2021-02-14T00:00:00\",\"2021-02-18T00:00:00\",\"2021-02-19T00:00:00\",\"2021-02-20T00:00:00\",\"2021-02-21T00:00:00\",\"2021-02-22T00:00:00\",\"2021-02-23T00:00:00\",\"2021-02-24T00:00:00\",\"2021-02-25T00:00:00\",\"2021-02-26T00:00:00\",\"2021-02-27T00:00:00\",\"2021-02-28T00:00:00\",\"2021-03-01T00:00:00\",\"2021-03-02T00:00:00\",\"2021-03-03T00:00:00\",\"2021-03-04T00:00:00\",\"2021-03-05T00:00:00\",\"2021-03-06T00:00:00\",\"2021-03-07T00:00:00\",\"2021-03-08T00:00:00\",\"2021-03-09T00:00:00\",\"2021-03-10T00:00:00\",\"2021-03-11T00:00:00\",\"2021-03-12T00:00:00\",\"2021-03-13T00:00:00\",\"2021-03-14T00:00:00\",\"2021-03-15T00:00:00\",\"2021-03-16T00:00:00\",\"2021-03-17T00:00:00\",\"2021-03-18T00:00:00\",\"2021-03-19T00:00:00\",\"2021-03-20T00:00:00\",\"2021-03-21T00:00:00\",\"2021-03-22T00:00:00\",\"2021-03-23T00:00:00\",\"2021-03-24T00:00:00\",\"2021-03-25T00:00:00\",\"2021-03-26T00:00:00\",\"2021-03-27T00:00:00\",\"2021-03-28T00:00:00\",\"2021-03-29T00:00:00\",\"2021-03-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-04-01T00:00:00\",\"2021-04-02T00:00:00\",\"2021-04-03T00:00:00\",\"2021-04-04T00:00:00\",\"2021-04-05T00:00:00\",\"2021-04-06T00:00:00\",\"2021-04-07T00:00:00\",\"2021-04-08T00:00:00\",\"2021-04-09T00:00:00\",\"2021-04-10T00:00:00\",\"2021-04-11T00:00:00\",\"2021-04-12T00:00:00\",\"2021-04-13T00:00:00\",\"2021-04-14T00:00:00\",\"2021-04-15T00:00:00\",\"2021-04-16T00:00:00\",\"2021-04-17T00:00:00\",\"2021-04-18T00:00:00\",\"2021-04-19T00:00:00\",\"2021-04-20T00:00:00\",\"2021-04-21T00:00:00\",\"2021-04-22T00:00:00\",\"2021-04-23T00:00:00\",\"2021-04-24T00:00:00\",\"2021-04-25T00:00:00\",\"2021-04-26T00:00:00\",\"2021-04-27T00:00:00\",\"2021-04-28T00:00:00\",\"2021-04-29T00:00:00\",\"2021-04-30T00:00:00\",\"2021-05-01T00:00:00\",\"2021-05-02T00:00:00\",\"2021-05-03T00:00:00\",\"2021-05-04T00:00:00\",\"2021-05-05T00:00:00\",\"2021-05-06T00:00:00\",\"2021-05-07T00:00:00\",\"2021-05-08T00:00:00\",\"2021-05-09T00:00:00\",\"2021-05-10T00:00:00\",\"2021-05-11T00:00:00\",\"2021-05-12T00:00:00\",\"2021-05-13T00:00:00\",\"2021-05-14T00:00:00\",\"2021-05-15T00:00:00\",\"2021-05-16T00:00:00\",\"2021-05-17T00:00:00\",\"2021-05-18T00:00:00\",\"2021-05-19T00:00:00\",\"2021-05-20T00:00:00\",\"2021-05-21T00:00:00\",\"2021-05-22T00:00:00\",\"2021-05-23T00:00:00\",\"2021-05-24T00:00:00\",\"2021-05-25T00:00:00\",\"2021-05-26T00:00:00\",\"2021-05-27T00:00:00\",\"2021-05-28T00:00:00\",\"2021-05-29T00:00:00\",\"2021-05-30T00:00:00\",\"2021-05-31T00:00:00\",\"2021-06-01T00:00:00\",\"2021-06-02T00:00:00\",\"2021-06-03T00:00:00\",\"2021-06-04T00:00:00\",\"2021-06-05T00:00:00\",\"2021-06-06T00:00:00\",\"2021-06-07T00:00:00\",\"2021-06-08T00:00:00\",\"2021-06-09T00:00:00\",\"2021-06-10T00:00:00\",\"2021-06-11T00:00:00\",\"2021-06-12T00:00:00\",\"2021-06-13T00:00:00\",\"2021-06-14T00:00:00\",\"2021-06-15T00:00:00\",\"2021-06-16T00:00:00\",\"2021-06-17T00:00:00\",\"2021-06-18T00:00:00\",\"2021-06-19T00:00:00\",\"2021-06-20T00:00:00\",\"2021-06-21T00:00:00\",\"2021-06-22T00:00:00\",\"2021-06-23T00:00:00\",\"2021-06-24T00:00:00\",\"2021-06-25T00:00:00\",\"2021-06-26T00:00:00\",\"2021-06-27T00:00:00\",\"2021-06-28T00:00:00\",\"2021-06-29T00:00:00\",\"2021-06-30T00:00:00\",\"2021-07-01T00:00:00\",\"2021-07-02T00:00:00\",\"2021-07-03T00:00:00\",\"2021-07-04T00:00:00\",\"2021-07-05T00:00:00\",\"2021-07-06T00:00:00\",\"2021-07-07T00:00:00\",\"2021-07-08T00:00:00\",\"2021-07-09T00:00:00\",\"2021-07-10T00:00:00\",\"2021-07-11T00:00:00\",\"2021-07-12T00:00:00\",\"2021-07-13T00:00:00\",\"2021-07-14T00:00:00\",\"2021-07-15T00:00:00\",\"2021-07-16T00:00:00\",\"2021-07-17T00:00:00\",\"2021-07-18T00:00:00\",\"2021-07-19T00:00:00\",\"2021-07-20T00:00:00\",\"2021-07-21T00:00:00\",\"2021-07-22T00:00:00\",\"2021-07-23T00:00:00\",\"2021-07-24T00:00:00\",\"2021-07-25T00:00:00\",\"2021-07-26T00:00:00\",\"2021-07-27T00:00:00\",\"2021-07-28T00:00:00\",\"2021-07-29T00:00:00\",\"2021-07-30T00:00:00\",\"2021-07-31T00:00:00\",\"2021-08-01T00:00:00\",\"2021-08-02T00:00:00\",\"2021-08-03T00:00:00\",\"2021-08-04T00:00:00\",\"2021-08-05T00:00:00\",\"2021-08-06T00:00:00\",\"2021-08-07T00:00:00\",\"2021-08-08T00:00:00\",\"2021-08-09T00:00:00\",\"2021-08-10T00:00:00\",\"2021-08-11T00:00:00\",\"2021-08-12T00:00:00\",\"2021-08-13T00:00:00\",\"2021-08-14T00:00:00\",\"2021-08-15T00:00:00\",\"2021-08-16T00:00:00\",\"2021-08-17T00:00:00\",\"2021-08-18T00:00:00\",\"2021-08-19T00:00:00\",\"2021-08-20T00:00:00\",\"2021-08-21T00:00:00\",\"2021-08-22T00:00:00\",\"2021-08-23T00:00:00\",\"2021-08-24T00:00:00\",\"2021-08-25T00:00:00\",\"2021-08-26T00:00:00\",\"2021-08-27T00:00:00\",\"2021-08-28T00:00:00\",\"2021-08-29T00:00:00\",\"2021-08-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-09-01T00:00:00\",\"2021-09-02T00:00:00\",\"2021-09-03T00:00:00\",\"2021-09-04T00:00:00\",\"2021-09-05T00:00:00\",\"2021-09-07T00:00:00\",\"2021-09-08T00:00:00\",\"2021-09-09T00:00:00\",\"2021-09-10T00:00:00\",\"2021-09-11T00:00:00\",\"2021-09-12T00:00:00\",\"2021-09-13T00:00:00\",\"2021-09-14T00:00:00\",\"2021-09-15T00:00:00\",\"2021-09-16T00:00:00\",\"2021-09-17T00:00:00\",\"2021-09-18T00:00:00\",\"2021-09-19T00:00:00\",\"2021-09-20T00:00:00\",\"2021-09-21T00:00:00\",\"2021-09-22T00:00:00\",\"2021-09-23T00:00:00\",\"2021-09-24T00:00:00\",\"2021-09-25T00:00:00\",\"2021-09-26T00:00:00\",\"2021-09-27T00:00:00\",\"2021-09-28T00:00:00\",\"2021-09-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-10-01T00:00:00\",\"2021-10-02T00:00:00\",\"2021-10-03T00:00:00\",\"2021-10-04T00:00:00\",\"2021-10-05T00:00:00\",\"2021-10-06T00:00:00\",\"2021-10-07T00:00:00\",\"2021-10-08T00:00:00\",\"2021-10-09T00:00:00\",\"2021-10-10T00:00:00\",\"2021-10-11T00:00:00\",\"2021-10-12T00:00:00\",\"2021-10-13T00:00:00\",\"2021-10-14T00:00:00\",\"2021-10-15T00:00:00\",\"2021-10-16T00:00:00\",\"2021-10-17T00:00:00\",\"2021-10-18T00:00:00\",\"2021-10-19T00:00:00\",\"2021-10-20T00:00:00\",\"2021-10-21T00:00:00\",\"2021-10-22T00:00:00\",\"2021-10-23T00:00:00\",\"2021-10-24T00:00:00\",\"2021-10-25T00:00:00\",\"2021-10-26T00:00:00\",\"2021-10-27T00:00:00\",\"2021-10-28T00:00:00\",\"2021-10-29T00:00:00\",\"2021-10-30T00:00:00\",\"2021-10-31T00:00:00\",\"2021-11-01T00:00:00\",\"2021-11-02T00:00:00\",\"2021-11-03T00:00:00\",\"2021-11-04T00:00:00\",\"2021-11-05T00:00:00\",\"2021-11-06T00:00:00\",\"2021-11-07T00:00:00\",\"2021-11-08T00:00:00\",\"2021-11-09T00:00:00\",\"2021-11-10T00:00:00\",\"2021-11-11T00:00:00\",\"2021-11-12T00:00:00\",\"2021-11-13T00:00:00\",\"2021-11-14T00:00:00\",\"2021-11-15T00:00:00\",\"2021-11-16T00:00:00\",\"2021-11-17T00:00:00\",\"2021-11-18T00:00:00\",\"2021-11-19T00:00:00\",\"2021-11-20T00:00:00\",\"2021-11-21T00:00:00\",\"2021-11-22T00:00:00\",\"2021-11-23T00:00:00\",\"2021-11-24T00:00:00\",\"2021-11-26T00:00:00\",\"2021-11-27T00:00:00\",\"2021-11-28T00:00:00\",\"2021-11-29T00:00:00\",\"2021-11-30T00:00:00\",\"2021-12-01T00:00:00\",\"2021-12-02T00:00:00\",\"2021-12-03T00:00:00\",\"2021-12-04T00:00:00\",\"2021-12-05T00:00:00\",\"2021-12-06T00:00:00\",\"2021-12-07T00:00:00\",\"2021-12-08T00:00:00\",\"2021-12-09T00:00:00\",\"2021-12-10T00:00:00\",\"2021-12-11T00:00:00\",\"2021-12-12T00:00:00\",\"2021-12-13T00:00:00\",\"2021-12-14T00:00:00\",\"2021-12-15T00:00:00\",\"2021-12-16T00:00:00\",\"2021-12-17T00:00:00\",\"2021-12-18T00:00:00\",\"2021-12-19T00:00:00\",\"2021-12-20T00:00:00\",\"2021-12-21T00:00:00\",\"2021-12-22T00:00:00\",\"2021-12-23T00:00:00\",\"2021-12-24T00:00:00\",\"2021-12-25T00:00:00\",\"2021-12-26T00:00:00\",\"2021-12-27T00:00:00\",\"2021-12-28T00:00:00\",\"2021-12-29T00:00:00\",\"2021-12-30T00:00:00\",\"2021-12-31T00:00:00\",\"2022-01-01T00:00:00\",\"2022-01-02T00:00:00\",\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-08T00:00:00\",\"2022-01-09T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-15T00:00:00\",\"2022-01-16T00:00:00\"],\"xaxis\":\"x\",\"y\":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"yaxis\":\"y\",\"type\":\"scattergl\"},{\"hovertemplate\":\"Animal Type_y=Other<br>Outcome Date=%{x}<br>count=%{y}<extra></extra>\",\"legendgroup\":\"Other\",\"line\":{\"color\":\"#FFA15A\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"Other\",\"showlegend\":true,\"x\":[\"2020-03-01T00:00:00\",\"2020-03-02T00:00:00\",\"2020-03-03T00:00:00\",\"2020-03-04T00:00:00\",\"2020-03-05T00:00:00\",\"2020-03-06T00:00:00\",\"2020-03-07T00:00:00\",\"2020-03-08T00:00:00\",\"2020-03-09T00:00:00\",\"2020-03-10T00:00:00\",\"2020-03-11T00:00:00\",\"2020-03-12T00:00:00\",\"2020-03-13T00:00:00\",\"2020-03-14T00:00:00\",\"2020-03-15T00:00:00\",\"2020-03-16T00:00:00\",\"2020-03-17T00:00:00\",\"2020-03-18T00:00:00\",\"2020-03-19T00:00:00\",\"2020-03-20T00:00:00\",\"2020-03-21T00:00:00\",\"2020-03-22T00:00:00\",\"2020-03-23T00:00:00\",\"2020-03-24T00:00:00\",\"2020-03-25T00:00:00\",\"2020-03-26T00:00:00\",\"2020-03-27T00:00:00\",\"2020-03-28T00:00:00\",\"2020-03-29T00:00:00\",\"2020-03-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-04-01T00:00:00\",\"2020-04-02T00:00:00\",\"2020-04-03T00:00:00\",\"2020-04-04T00:00:00\",\"2020-04-05T00:00:00\",\"2020-04-06T00:00:00\",\"2020-04-07T00:00:00\",\"2020-04-08T00:00:00\",\"2020-04-09T00:00:00\",\"2020-04-10T00:00:00\",\"2020-04-11T00:00:00\",\"2020-04-12T00:00:00\",\"2020-04-13T00:00:00\",\"2020-04-14T00:00:00\",\"2020-04-15T00:00:00\",\"2020-04-16T00:00:00\",\"2020-04-17T00:00:00\",\"2020-04-18T00:00:00\",\"2020-04-19T00:00:00\",\"2020-04-20T00:00:00\",\"2020-04-21T00:00:00\",\"2020-04-22T00:00:00\",\"2020-04-23T00:00:00\",\"2020-04-24T00:00:00\",\"2020-04-25T00:00:00\",\"2020-04-26T00:00:00\",\"2020-04-27T00:00:00\",\"2020-04-28T00:00:00\",\"2020-04-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-05-01T00:00:00\",\"2020-05-02T00:00:00\",\"2020-05-03T00:00:00\",\"2020-05-04T00:00:00\",\"2020-05-05T00:00:00\",\"2020-05-06T00:00:00\",\"2020-05-07T00:00:00\",\"2020-05-08T00:00:00\",\"2020-05-09T00:00:00\",\"2020-05-10T00:00:00\",\"2020-05-11T00:00:00\",\"2020-05-12T00:00:00\",\"2020-05-13T00:00:00\",\"2020-05-14T00:00:00\",\"2020-05-15T00:00:00\",\"2020-05-16T00:00:00\",\"2020-05-17T00:00:00\",\"2020-05-18T00:00:00\",\"2020-05-19T00:00:00\",\"2020-05-20T00:00:00\",\"2020-05-21T00:00:00\",\"2020-05-22T00:00:00\",\"2020-05-23T00:00:00\",\"2020-05-24T00:00:00\",\"2020-05-25T00:00:00\",\"2020-05-26T00:00:00\",\"2020-05-27T00:00:00\",\"2020-05-28T00:00:00\",\"2020-05-29T00:00:00\",\"2020-05-30T00:00:00\",\"2020-05-31T00:00:00\",\"2020-06-01T00:00:00\",\"2020-06-02T00:00:00\",\"2020-06-03T00:00:00\",\"2020-06-04T00:00:00\",\"2020-06-05T00:00:00\",\"2020-06-06T00:00:00\",\"2020-06-07T00:00:00\",\"2020-06-08T00:00:00\",\"2020-06-09T00:00:00\",\"2020-06-10T00:00:00\",\"2020-06-11T00:00:00\",\"2020-06-12T00:00:00\",\"2020-06-13T00:00:00\",\"2020-06-14T00:00:00\",\"2020-06-15T00:00:00\",\"2020-06-16T00:00:00\",\"2020-06-17T00:00:00\",\"2020-06-18T00:00:00\",\"2020-06-19T00:00:00\",\"2020-06-20T00:00:00\",\"2020-06-21T00:00:00\",\"2020-06-22T00:00:00\",\"2020-06-23T00:00:00\",\"2020-06-24T00:00:00\",\"2020-06-25T00:00:00\",\"2020-06-26T00:00:00\",\"2020-06-27T00:00:00\",\"2020-06-28T00:00:00\",\"2020-06-29T00:00:00\",\"2020-06-30T00:00:00\",\"2020-07-01T00:00:00\",\"2020-07-02T00:00:00\",\"2020-07-03T00:00:00\",\"2020-07-04T00:00:00\",\"2020-07-05T00:00:00\",\"2020-07-06T00:00:00\",\"2020-07-07T00:00:00\",\"2020-07-08T00:00:00\",\"2020-07-09T00:00:00\",\"2020-07-10T00:00:00\",\"2020-07-11T00:00:00\",\"2020-07-12T00:00:00\",\"2020-07-13T00:00:00\",\"2020-07-14T00:00:00\",\"2020-07-15T00:00:00\",\"2020-07-16T00:00:00\",\"2020-07-17T00:00:00\",\"2020-07-18T00:00:00\",\"2020-07-19T00:00:00\",\"2020-07-20T00:00:00\",\"2020-07-21T00:00:00\",\"2020-07-22T00:00:00\",\"2020-07-23T00:00:00\",\"2020-07-24T00:00:00\",\"2020-07-25T00:00:00\",\"2020-07-26T00:00:00\",\"2020-07-27T00:00:00\",\"2020-07-28T00:00:00\",\"2020-07-29T00:00:00\",\"2020-07-30T00:00:00\",\"2020-07-31T00:00:00\",\"2020-08-01T00:00:00\",\"2020-08-02T00:00:00\",\"2020-08-03T00:00:00\",\"2020-08-04T00:00:00\",\"2020-08-05T00:00:00\",\"2020-08-06T00:00:00\",\"2020-08-07T00:00:00\",\"2020-08-08T00:00:00\",\"2020-08-09T00:00:00\",\"2020-08-10T00:00:00\",\"2020-08-11T00:00:00\",\"2020-08-12T00:00:00\",\"2020-08-13T00:00:00\",\"2020-08-14T00:00:00\",\"2020-08-15T00:00:00\",\"2020-08-16T00:00:00\",\"2020-08-17T00:00:00\",\"2020-08-18T00:00:00\",\"2020-08-19T00:00:00\",\"2020-08-20T00:00:00\",\"2020-08-21T00:00:00\",\"2020-08-22T00:00:00\",\"2020-08-23T00:00:00\",\"2020-08-24T00:00:00\",\"2020-08-25T00:00:00\",\"2020-08-26T00:00:00\",\"2020-08-27T00:00:00\",\"2020-08-28T00:00:00\",\"2020-08-29T00:00:00\",\"2020-08-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-09-01T00:00:00\",\"2020-09-02T00:00:00\",\"2020-09-03T00:00:00\",\"2020-09-04T00:00:00\",\"2020-09-05T00:00:00\",\"2020-09-06T00:00:00\",\"2020-09-07T00:00:00\",\"2020-09-08T00:00:00\",\"2020-09-09T00:00:00\",\"2020-09-10T00:00:00\",\"2020-09-11T00:00:00\",\"2020-09-12T00:00:00\",\"2020-09-13T00:00:00\",\"2020-09-14T00:00:00\",\"2020-09-15T00:00:00\",\"2020-09-16T00:00:00\",\"2020-09-17T00:00:00\",\"2020-09-18T00:00:00\",\"2020-09-19T00:00:00\",\"2020-09-20T00:00:00\",\"2020-09-21T00:00:00\",\"2020-09-22T00:00:00\",\"2020-09-23T00:00:00\",\"2020-09-24T00:00:00\",\"2020-09-25T00:00:00\",\"2020-09-26T00:00:00\",\"2020-09-27T00:00:00\",\"2020-09-28T00:00:00\",\"2020-09-29T00:00:00\",\"2020-09-30T00:00:00\",\"2020-10-01T00:00:00\",\"2020-10-02T00:00:00\",\"2020-10-03T00:00:00\",\"2020-10-04T00:00:00\",\"2020-10-05T00:00:00\",\"2020-10-06T00:00:00\",\"2020-10-07T00:00:00\",\"2020-10-08T00:00:00\",\"2020-10-09T00:00:00\",\"2020-10-10T00:00:00\",\"2020-10-11T00:00:00\",\"2020-10-12T00:00:00\",\"2020-10-13T00:00:00\",\"2020-10-14T00:00:00\",\"2020-10-15T00:00:00\",\"2020-10-16T00:00:00\",\"2020-10-17T00:00:00\",\"2020-10-18T00:00:00\",\"2020-10-19T00:00:00\",\"2020-10-20T00:00:00\",\"2020-10-21T00:00:00\",\"2020-10-22T00:00:00\",\"2020-10-23T00:00:00\",\"2020-10-24T00:00:00\",\"2020-10-25T00:00:00\",\"2020-10-26T00:00:00\",\"2020-10-27T00:00:00\",\"2020-10-28T00:00:00\",\"2020-10-29T00:00:00\",\"2020-10-30T00:00:00\",\"2020-10-31T00:00:00\",\"2020-11-01T00:00:00\",\"2020-11-02T00:00:00\",\"2020-11-03T00:00:00\",\"2020-11-04T00:00:00\",\"2020-11-05T00:00:00\",\"2020-11-06T00:00:00\",\"2020-11-07T00:00:00\",\"2020-11-08T00:00:00\",\"2020-11-09T00:00:00\",\"2020-11-10T00:00:00\",\"2020-11-12T00:00:00\",\"2020-11-13T00:00:00\",\"2020-11-14T00:00:00\",\"2020-11-15T00:00:00\",\"2020-11-16T00:00:00\",\"2020-11-17T00:00:00\",\"2020-11-18T00:00:00\",\"2020-11-19T00:00:00\",\"2020-11-20T00:00:00\",\"2020-11-21T00:00:00\",\"2020-11-22T00:00:00\",\"2020-11-23T00:00:00\",\"2020-11-24T00:00:00\",\"2020-11-25T00:00:00\",\"2020-11-26T00:00:00\",\"2020-11-27T00:00:00\",\"2020-11-28T00:00:00\",\"2020-11-29T00:00:00\",\"2020-11-30T00:00:00\",\"2020-12-01T00:00:00\",\"2020-12-02T00:00:00\",\"2020-12-03T00:00:00\",\"2020-12-04T00:00:00\",\"2020-12-05T00:00:00\",\"2020-12-06T00:00:00\",\"2020-12-07T00:00:00\",\"2020-12-08T00:00:00\",\"2020-12-09T00:00:00\",\"2020-12-10T00:00:00\",\"2020-12-11T00:00:00\",\"2020-12-12T00:00:00\",\"2020-12-13T00:00:00\",\"2020-12-14T00:00:00\",\"2020-12-15T00:00:00\",\"2020-12-16T00:00:00\",\"2020-12-17T00:00:00\",\"2020-12-18T00:00:00\",\"2020-12-19T00:00:00\",\"2020-12-20T00:00:00\",\"2020-12-21T00:00:00\",\"2020-12-22T00:00:00\",\"2020-12-23T00:00:00\",\"2020-12-24T00:00:00\",\"2020-12-26T00:00:00\",\"2020-12-27T00:00:00\",\"2020-12-28T00:00:00\",\"2020-12-29T00:00:00\",\"2020-12-30T00:00:00\",\"2020-12-31T00:00:00\",\"2021-01-02T00:00:00\",\"2021-01-03T00:00:00\",\"2021-01-04T00:00:00\",\"2021-01-05T00:00:00\",\"2021-01-06T00:00:00\",\"2021-01-07T00:00:00\",\"2021-01-08T00:00:00\",\"2021-01-09T00:00:00\",\"2021-01-10T00:00:00\",\"2021-01-11T00:00:00\",\"2021-01-12T00:00:00\",\"2021-01-13T00:00:00\",\"2021-01-14T00:00:00\",\"2021-01-15T00:00:00\",\"2021-01-16T00:00:00\",\"2021-01-17T00:00:00\",\"2021-01-18T00:00:00\",\"2021-01-19T00:00:00\",\"2021-01-20T00:00:00\",\"2021-01-21T00:00:00\",\"2021-01-22T00:00:00\",\"2021-01-23T00:00:00\",\"2021-01-24T00:00:00\",\"2021-01-25T00:00:00\",\"2021-01-26T00:00:00\",\"2021-01-27T00:00:00\",\"2021-01-28T00:00:00\",\"2021-01-29T00:00:00\",\"2021-01-30T00:00:00\",\"2021-01-31T00:00:00\",\"2021-02-01T00:00:00\",\"2021-02-02T00:00:00\",\"2021-02-03T00:00:00\",\"2021-02-04T00:00:00\",\"2021-02-05T00:00:00\",\"2021-02-06T00:00:00\",\"2021-02-07T00:00:00\",\"2021-02-08T00:00:00\",\"2021-02-09T00:00:00\",\"2021-02-10T00:00:00\",\"2021-02-11T00:00:00\",\"2021-02-12T00:00:00\",\"2021-02-13T00:00:00\",\"2021-02-14T00:00:00\",\"2021-02-18T00:00:00\",\"2021-02-19T00:00:00\",\"2021-02-20T00:00:00\",\"2021-02-21T00:00:00\",\"2021-02-22T00:00:00\",\"2021-02-23T00:00:00\",\"2021-02-24T00:00:00\",\"2021-02-25T00:00:00\",\"2021-02-26T00:00:00\",\"2021-02-27T00:00:00\",\"2021-02-28T00:00:00\",\"2021-03-01T00:00:00\",\"2021-03-02T00:00:00\",\"2021-03-03T00:00:00\",\"2021-03-04T00:00:00\",\"2021-03-05T00:00:00\",\"2021-03-06T00:00:00\",\"2021-03-07T00:00:00\",\"2021-03-08T00:00:00\",\"2021-03-09T00:00:00\",\"2021-03-10T00:00:00\",\"2021-03-11T00:00:00\",\"2021-03-12T00:00:00\",\"2021-03-13T00:00:00\",\"2021-03-14T00:00:00\",\"2021-03-15T00:00:00\",\"2021-03-16T00:00:00\",\"2021-03-17T00:00:00\",\"2021-03-18T00:00:00\",\"2021-03-19T00:00:00\",\"2021-03-20T00:00:00\",\"2021-03-21T00:00:00\",\"2021-03-22T00:00:00\",\"2021-03-23T00:00:00\",\"2021-03-24T00:00:00\",\"2021-03-25T00:00:00\",\"2021-03-26T00:00:00\",\"2021-03-27T00:00:00\",\"2021-03-28T00:00:00\",\"2021-03-29T00:00:00\",\"2021-03-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-04-01T00:00:00\",\"2021-04-02T00:00:00\",\"2021-04-03T00:00:00\",\"2021-04-04T00:00:00\",\"2021-04-05T00:00:00\",\"2021-04-06T00:00:00\",\"2021-04-07T00:00:00\",\"2021-04-08T00:00:00\",\"2021-04-09T00:00:00\",\"2021-04-10T00:00:00\",\"2021-04-11T00:00:00\",\"2021-04-12T00:00:00\",\"2021-04-13T00:00:00\",\"2021-04-14T00:00:00\",\"2021-04-15T00:00:00\",\"2021-04-16T00:00:00\",\"2021-04-17T00:00:00\",\"2021-04-18T00:00:00\",\"2021-04-19T00:00:00\",\"2021-04-20T00:00:00\",\"2021-04-21T00:00:00\",\"2021-04-22T00:00:00\",\"2021-04-23T00:00:00\",\"2021-04-24T00:00:00\",\"2021-04-25T00:00:00\",\"2021-04-26T00:00:00\",\"2021-04-27T00:00:00\",\"2021-04-28T00:00:00\",\"2021-04-29T00:00:00\",\"2021-04-30T00:00:00\",\"2021-05-01T00:00:00\",\"2021-05-02T00:00:00\",\"2021-05-03T00:00:00\",\"2021-05-04T00:00:00\",\"2021-05-05T00:00:00\",\"2021-05-06T00:00:00\",\"2021-05-07T00:00:00\",\"2021-05-08T00:00:00\",\"2021-05-09T00:00:00\",\"2021-05-10T00:00:00\",\"2021-05-11T00:00:00\",\"2021-05-12T00:00:00\",\"2021-05-13T00:00:00\",\"2021-05-14T00:00:00\",\"2021-05-15T00:00:00\",\"2021-05-16T00:00:00\",\"2021-05-17T00:00:00\",\"2021-05-18T00:00:00\",\"2021-05-19T00:00:00\",\"2021-05-20T00:00:00\",\"2021-05-21T00:00:00\",\"2021-05-22T00:00:00\",\"2021-05-23T00:00:00\",\"2021-05-24T00:00:00\",\"2021-05-25T00:00:00\",\"2021-05-26T00:00:00\",\"2021-05-27T00:00:00\",\"2021-05-28T00:00:00\",\"2021-05-29T00:00:00\",\"2021-05-30T00:00:00\",\"2021-05-31T00:00:00\",\"2021-06-01T00:00:00\",\"2021-06-02T00:00:00\",\"2021-06-03T00:00:00\",\"2021-06-04T00:00:00\",\"2021-06-05T00:00:00\",\"2021-06-06T00:00:00\",\"2021-06-07T00:00:00\",\"2021-06-08T00:00:00\",\"2021-06-09T00:00:00\",\"2021-06-10T00:00:00\",\"2021-06-11T00:00:00\",\"2021-06-12T00:00:00\",\"2021-06-13T00:00:00\",\"2021-06-14T00:00:00\",\"2021-06-15T00:00:00\",\"2021-06-16T00:00:00\",\"2021-06-17T00:00:00\",\"2021-06-18T00:00:00\",\"2021-06-19T00:00:00\",\"2021-06-20T00:00:00\",\"2021-06-21T00:00:00\",\"2021-06-22T00:00:00\",\"2021-06-23T00:00:00\",\"2021-06-24T00:00:00\",\"2021-06-25T00:00:00\",\"2021-06-26T00:00:00\",\"2021-06-27T00:00:00\",\"2021-06-28T00:00:00\",\"2021-06-29T00:00:00\",\"2021-06-30T00:00:00\",\"2021-07-01T00:00:00\",\"2021-07-02T00:00:00\",\"2021-07-03T00:00:00\",\"2021-07-04T00:00:00\",\"2021-07-05T00:00:00\",\"2021-07-06T00:00:00\",\"2021-07-07T00:00:00\",\"2021-07-08T00:00:00\",\"2021-07-09T00:00:00\",\"2021-07-10T00:00:00\",\"2021-07-11T00:00:00\",\"2021-07-12T00:00:00\",\"2021-07-13T00:00:00\",\"2021-07-14T00:00:00\",\"2021-07-15T00:00:00\",\"2021-07-16T00:00:00\",\"2021-07-17T00:00:00\",\"2021-07-18T00:00:00\",\"2021-07-19T00:00:00\",\"2021-07-20T00:00:00\",\"2021-07-21T00:00:00\",\"2021-07-22T00:00:00\",\"2021-07-23T00:00:00\",\"2021-07-24T00:00:00\",\"2021-07-25T00:00:00\",\"2021-07-26T00:00:00\",\"2021-07-27T00:00:00\",\"2021-07-28T00:00:00\",\"2021-07-29T00:00:00\",\"2021-07-30T00:00:00\",\"2021-07-31T00:00:00\",\"2021-08-01T00:00:00\",\"2021-08-02T00:00:00\",\"2021-08-03T00:00:00\",\"2021-08-04T00:00:00\",\"2021-08-05T00:00:00\",\"2021-08-06T00:00:00\",\"2021-08-07T00:00:00\",\"2021-08-08T00:00:00\",\"2021-08-09T00:00:00\",\"2021-08-10T00:00:00\",\"2021-08-11T00:00:00\",\"2021-08-12T00:00:00\",\"2021-08-13T00:00:00\",\"2021-08-14T00:00:00\",\"2021-08-15T00:00:00\",\"2021-08-16T00:00:00\",\"2021-08-17T00:00:00\",\"2021-08-18T00:00:00\",\"2021-08-19T00:00:00\",\"2021-08-20T00:00:00\",\"2021-08-21T00:00:00\",\"2021-08-22T00:00:00\",\"2021-08-23T00:00:00\",\"2021-08-24T00:00:00\",\"2021-08-25T00:00:00\",\"2021-08-26T00:00:00\",\"2021-08-27T00:00:00\",\"2021-08-28T00:00:00\",\"2021-08-29T00:00:00\",\"2021-08-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-09-01T00:00:00\",\"2021-09-02T00:00:00\",\"2021-09-03T00:00:00\",\"2021-09-04T00:00:00\",\"2021-09-05T00:00:00\",\"2021-09-07T00:00:00\",\"2021-09-08T00:00:00\",\"2021-09-09T00:00:00\",\"2021-09-10T00:00:00\",\"2021-09-11T00:00:00\",\"2021-09-12T00:00:00\",\"2021-09-13T00:00:00\",\"2021-09-14T00:00:00\",\"2021-09-15T00:00:00\",\"2021-09-16T00:00:00\",\"2021-09-17T00:00:00\",\"2021-09-18T00:00:00\",\"2021-09-19T00:00:00\",\"2021-09-20T00:00:00\",\"2021-09-21T00:00:00\",\"2021-09-22T00:00:00\",\"2021-09-23T00:00:00\",\"2021-09-24T00:00:00\",\"2021-09-25T00:00:00\",\"2021-09-26T00:00:00\",\"2021-09-27T00:00:00\",\"2021-09-28T00:00:00\",\"2021-09-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-10-01T00:00:00\",\"2021-10-02T00:00:00\",\"2021-10-03T00:00:00\",\"2021-10-04T00:00:00\",\"2021-10-05T00:00:00\",\"2021-10-06T00:00:00\",\"2021-10-07T00:00:00\",\"2021-10-08T00:00:00\",\"2021-10-09T00:00:00\",\"2021-10-10T00:00:00\",\"2021-10-11T00:00:00\",\"2021-10-12T00:00:00\",\"2021-10-13T00:00:00\",\"2021-10-14T00:00:00\",\"2021-10-15T00:00:00\",\"2021-10-16T00:00:00\",\"2021-10-17T00:00:00\",\"2021-10-18T00:00:00\",\"2021-10-19T00:00:00\",\"2021-10-20T00:00:00\",\"2021-10-21T00:00:00\",\"2021-10-22T00:00:00\",\"2021-10-23T00:00:00\",\"2021-10-24T00:00:00\",\"2021-10-25T00:00:00\",\"2021-10-26T00:00:00\",\"2021-10-27T00:00:00\",\"2021-10-28T00:00:00\",\"2021-10-29T00:00:00\",\"2021-10-30T00:00:00\",\"2021-10-31T00:00:00\",\"2021-11-01T00:00:00\",\"2021-11-02T00:00:00\",\"2021-11-03T00:00:00\",\"2021-11-04T00:00:00\",\"2021-11-05T00:00:00\",\"2021-11-06T00:00:00\",\"2021-11-07T00:00:00\",\"2021-11-08T00:00:00\",\"2021-11-09T00:00:00\",\"2021-11-10T00:00:00\",\"2021-11-11T00:00:00\",\"2021-11-12T00:00:00\",\"2021-11-13T00:00:00\",\"2021-11-14T00:00:00\",\"2021-11-15T00:00:00\",\"2021-11-16T00:00:00\",\"2021-11-17T00:00:00\",\"2021-11-18T00:00:00\",\"2021-11-19T00:00:00\",\"2021-11-20T00:00:00\",\"2021-11-21T00:00:00\",\"2021-11-22T00:00:00\",\"2021-11-23T00:00:00\",\"2021-11-24T00:00:00\",\"2021-11-26T00:00:00\",\"2021-11-27T00:00:00\",\"2021-11-28T00:00:00\",\"2021-11-29T00:00:00\",\"2021-11-30T00:00:00\",\"2021-12-01T00:00:00\",\"2021-12-02T00:00:00\",\"2021-12-03T00:00:00\",\"2021-12-04T00:00:00\",\"2021-12-05T00:00:00\",\"2021-12-06T00:00:00\",\"2021-12-07T00:00:00\",\"2021-12-08T00:00:00\",\"2021-12-09T00:00:00\",\"2021-12-10T00:00:00\",\"2021-12-11T00:00:00\",\"2021-12-12T00:00:00\",\"2021-12-13T00:00:00\",\"2021-12-14T00:00:00\",\"2021-12-15T00:00:00\",\"2021-12-16T00:00:00\",\"2021-12-17T00:00:00\",\"2021-12-18T00:00:00\",\"2021-12-19T00:00:00\",\"2021-12-20T00:00:00\",\"2021-12-21T00:00:00\",\"2021-12-22T00:00:00\",\"2021-12-23T00:00:00\",\"2021-12-24T00:00:00\",\"2021-12-25T00:00:00\",\"2021-12-26T00:00:00\",\"2021-12-27T00:00:00\",\"2021-12-28T00:00:00\",\"2021-12-29T00:00:00\",\"2021-12-30T00:00:00\",\"2021-12-31T00:00:00\",\"2022-01-01T00:00:00\",\"2022-01-02T00:00:00\",\"2022-01-03T00:00:00\",\"2022-01-04T00:00:00\",\"2022-01-05T00:00:00\",\"2022-01-06T00:00:00\",\"2022-01-07T00:00:00\",\"2022-01-08T00:00:00\",\"2022-01-09T00:00:00\",\"2022-01-10T00:00:00\",\"2022-01-11T00:00:00\",\"2022-01-12T00:00:00\",\"2022-01-13T00:00:00\",\"2022-01-14T00:00:00\",\"2022-01-15T00:00:00\",\"2022-01-16T00:00:00\"],\"xaxis\":\"x\",\"y\":[14,6,4,3,5,4,2,2,3,1,3,6,0,1,8,7,4,3,9,2,0,4,4,7,5,4,4,2,5,5,3,1,3,0,2,3,0,0,2,0,3,0,3,0,6,3,0,2,3,5,1,2,0,0,0,0,2,0,0,0,5,0,0,2,1,0,1,2,1,0,1,0,0,1,0,0,2,1,2,2,0,1,1,0,5,0,1,0,0,0,0,2,0,0,0,1,1,2,1,1,1,0,2,1,0,7,7,2,1,1,0,2,1,2,4,1,0,0,1,7,3,4,5,1,1,1,1,1,0,3,0,2,0,1,2,1,1,1,0,0,1,2,0,2,2,3,3,1,1,7,2,0,7,0,1,4,4,1,1,3,0,2,1,1,1,8,1,0,4,1,0,6,3,3,1,12,1,0,2,2,1,3,1,3,0,0,3,1,1,0,1,1,1,2,0,0,1,2,0,1,5,2,0,3,0,1,0,1,4,0,2,2,1,5,2,2,3,2,2,4,1,0,1,0,2,4,0,2,5,1,2,3,1,4,0,1,0,1,6,1,4,0,0,1,0,0,12,1,0,2,0,3,0,1,3,1,0,0,6,1,1,2,1,1,1,3,1,1,0,5,0,3,1,1,0,2,1,0,1,1,2,1,0,0,1,2,0,0,1,0,7,2,1,3,2,0,0,1,1,0,0,0,0,3,0,2,1,0,0,14,1,2,1,1,1,1,2,1,0,1,0,1,2,1,0,0,1,0,2,2,5,1,1,1,0,1,1,1,1,0,1,0,4,3,0,0,1,1,0,0,0,1,0,1,1,8,0,1,3,1,3,2,7,1,1,7,2,4,2,4,0,2,3,2,5,3,2,3,1,5,4,2,2,7,0,0,3,3,3,3,5,1,3,4,2,0,6,5,5,2,0,0,2,2,2,2,0,4,0,3,3,2,1,0,0,14,1,0,6,2,2,1,5,0,1,1,4,0,4,3,0,0,2,2,1,0,1,3,1,2,1,1,0,6,1,0,2,0,2,0,0,0,1,1,1,0,3,0,1,2,1,0,0,1,1,5,0,11,4,2,2,2,1,1,2,2,3,6,0,4,1,0,0,1,5,0,4,1,1,2,0,0,5,0,0,2,4,1,1,1,1,2,2,0,0,2,1,1,2,0,3,1,0,0,0,2,0,4,1,1,0,0,0,14,4,3,0,0,1,1,1,0,0,1,2,1,1,1,5,1,2,0,2,3,1,1,1,3,2,3,4,2,2,1,1,0,6,6,2,2,2,3,0,1,1,2,14,2,0,3,1,3,4,3,6,3,4,5,2,2,1,5,1,0,2,1,2,0,4,2,2,2,1,0,0,4,0,3,5,2,1,1,1,0,1,2,0,2,1,4,2,2,1,0,2,4,1,3,3,0,1,0,3,2,1,2,0,0,4,1,0,0,0,0,0,0,0,1,1,1,6,0,0,1,0,1,1,2,0,2,1,0,0,5,1,0,0,0,1,0,0,0,6,3,1,1,2,0,1,4,2,3,1,0,1,1,1,0,1],\"yaxis\":\"y\",\"type\":\"scattergl\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Outcome Date\"},\"rangeslider\":{\"visible\":true},\"rangeselector\":{\"buttons\":[{\"count\":1,\"label\":\"1m\",\"step\":\"month\",\"stepmode\":\"backward\"},{\"count\":6,\"label\":\"6m\",\"step\":\"month\",\"stepmode\":\"backward\"},{\"count\":1,\"label\":\"YTD\",\"step\":\"year\",\"stepmode\":\"todate\"},{\"count\":1,\"label\":\"1y\",\"step\":\"year\",\"stepmode\":\"backward\"},{\"step\":\"all\"}]}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"count\"}},\"legend\":{\"title\":{\"text\":\"Animal Type_y\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('d12f7856-3726-4e76-a218-4eb26dc3a40c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## How many pets were adopted during the pandemic? March 2020-now\n",
    "\n",
    "### First, I need to query the data rows that are only March 2020-now\n",
    "Austin_2020UP = Austin_Data.loc[Austin_Data['Outcome Date'] >= '2020-03-01']\n",
    "Austin_2020UP\n",
    "group = Austin_2020UP.reset_index().groupby(['Outcome Date', 'Animal Type_y'], as_index=False).count().rename(columns={'index': 'count'})\n",
    "group = group.drop(columns=['Animal ID', 'Name_x',\n",
    "       'DateTime_x', 'Found Location', 'Intake Type', 'Intake Condition',\n",
    "       'Animal Type_x', 'Sex upon Intake', 'Age upon Intake', 'Breed_x',\n",
    "       'Color_x', 'Name_y', 'DateTime_y', 'Date of Birth', 'Outcome Type',\n",
    "       'Outcome Subtype', 'Sex upon Outcome', 'Age upon Outcome', 'Breed_y',\n",
    "       'Color_y', 'Intake Date', 'Outcome Month', 'Intake Month'])\n",
    "group['Outcome Date'] = pd.to_datetime(group['Outcome Date'])\n",
    "group['Year'] = group['Outcome Date'].dt.year\n",
    "fig = px.line(group, x='Outcome Date', y='count', color='Animal Type_y')\n",
    "fig.update_xaxes(\n",
    "    rangeslider_visible=True,\n",
    "    rangeselector=dict(\n",
    "        buttons=list([\n",
    "            dict(count=1, label=\"1m\", step=\"month\", stepmode=\"backward\"),\n",
    "            dict(count=6, label=\"6m\", step=\"month\", stepmode=\"backward\"),\n",
    "            dict(count=1, label=\"YTD\", step=\"year\", stepmode=\"todate\"),\n",
    "            dict(count=1, label=\"1y\", step=\"year\", stepmode=\"backward\"),\n",
    "            dict(step=\"all\")\n",
    "        ])\n",
    "    )\n",
    ")\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb0c7082",
   "metadata": {
    "papermill": {
     "duration": 0.067258,
     "end_time": "2024-10-11T19:10:40.860904",
     "exception": false,
     "start_time": "2024-10-11T19:10:40.793646",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Then created separate groups based on Animal Type to do a deeper dive"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aea51e1e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.004462Z",
     "iopub.status.busy": "2024-10-11T19:10:41.003265Z",
     "iopub.status.idle": "2024-10-11T19:10:41.024866Z",
     "shell.execute_reply": "2024-10-11T19:10:41.025480Z",
     "shell.execute_reply.started": "2022-12-16T15:22:56.952279Z"
    },
    "papermill": {
     "duration": 0.097025,
     "end_time": "2024-10-11T19:10:41.025712",
     "exception": false,
     "start_time": "2024-10-11T19:10:40.928687",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "Dog = Austin_2020UP[Austin_2020UP['Animal Type_x'] == 'Dog']\n",
    "Cat = Austin_2020UP[Austin_2020UP['Animal Type_x'] == 'Cat']\n",
    "Other = Austin_2020UP[Austin_2020UP['Animal Type_x'] == 'Other']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f573d6b4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.175093Z",
     "iopub.status.busy": "2024-10-11T19:10:41.170887Z",
     "iopub.status.idle": "2024-10-11T19:10:41.188276Z",
     "shell.execute_reply": "2024-10-11T19:10:41.187556Z",
     "shell.execute_reply.started": "2022-12-16T15:22:58.722862Z"
    },
    "papermill": {
     "duration": 0.093223,
     "end_time": "2024-10-11T19:10:41.188473",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.095250",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Chose to focus on the Dog Dataset\n",
    "Dog = Dog.rename(columns={'Name_x': 'Name', 'Breed_x': 'Breed', 'Animal Type_y': 'Animal_Type', 'Color_y': 'Color'})\n",
    "Dog = Dog.drop(columns=['Animal Type_x', 'Breed_y', 'DateTime_x', 'Color_x', 'Name_y', 'DateTime_y'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b2cd7559",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.349178Z",
     "iopub.status.busy": "2024-10-11T19:10:41.346383Z",
     "iopub.status.idle": "2024-10-11T19:10:41.371781Z",
     "shell.execute_reply": "2024-10-11T19:10:41.372411Z",
     "shell.execute_reply.started": "2022-12-16T15:23:00.409387Z"
    },
    "papermill": {
     "duration": 0.11574,
     "end_time": "2024-10-11T19:10:41.372649",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.256909",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Calculated duration between intake and outcome then forgot about it in later analysis\n",
    "Dog['Intake Date'] = pd.to_datetime(Dog['Intake Date'])\n",
    "Dog['Outcome Date'] = pd.to_datetime(Dog['Outcome Date'])\n",
    "Dog['Stay_Duration'] = Dog['Outcome Date'] - Dog['Intake Date']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "50c3cb74",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.517531Z",
     "iopub.status.busy": "2024-10-11T19:10:41.516564Z",
     "iopub.status.idle": "2024-10-11T19:10:41.520378Z",
     "shell.execute_reply": "2024-10-11T19:10:41.520963Z",
     "shell.execute_reply.started": "2022-12-16T15:23:01.541786Z"
    },
    "papermill": {
     "duration": 0.080557,
     "end_time": "2024-10-11T19:10:41.521221",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.440664",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Timedelta('109 days 05:59:26.416961130')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Dog['Stay_Duration'].mean() #2939 Days for max, -674 days for min, 109 days for mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7f29fbb1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.705253Z",
     "iopub.status.busy": "2024-10-11T19:10:41.704278Z",
     "iopub.status.idle": "2024-10-11T19:10:41.709582Z",
     "shell.execute_reply": "2024-10-11T19:10:41.708791Z",
     "shell.execute_reply.started": "2022-12-16T15:23:11.82532Z"
    },
    "papermill": {
     "duration": 0.118375,
     "end_time": "2024-10-11T19:10:41.709758",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.591383",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Found Location</th>\n",
       "      <th>Intake Type</th>\n",
       "      <th>Intake Condition</th>\n",
       "      <th>Sex upon Intake</th>\n",
       "      <th>Age upon Intake</th>\n",
       "      <th>Breed</th>\n",
       "      <th>Date of Birth</th>\n",
       "      <th>Outcome Type</th>\n",
       "      <th>Outcome Subtype</th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Sex upon Outcome</th>\n",
       "      <th>Age upon Outcome</th>\n",
       "      <th>Color</th>\n",
       "      <th>Intake Date</th>\n",
       "      <th>Outcome Date</th>\n",
       "      <th>Intake Month</th>\n",
       "      <th>Outcome Month</th>\n",
       "      <th>Stay_Duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>A836850</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>6111 Softwood Drive in Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Pregnant</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>06/15/2017</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Blue/White</td>\n",
       "      <td>2021-06-15</td>\n",
       "      <td>2021-06-16</td>\n",
       "      <td>June 2021</td>\n",
       "      <td>June 2021</td>\n",
       "      <td>1 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>A815227</td>\n",
       "      <td>Baby</td>\n",
       "      <td>12305 Zeller Lane in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Norfolk Terrier</td>\n",
       "      <td>01/12/2020</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Brown/Cream</td>\n",
       "      <td>2020-03-12</td>\n",
       "      <td>2020-03-13</td>\n",
       "      <td>March 2020</td>\n",
       "      <td>March 2020</td>\n",
       "      <td>1 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>Thaxton And Sassman in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>1 year</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2019-01-07</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>January 2019</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>636 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>1709 Colony Creek Drive in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>5 months</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2018-05-23</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>May 2018</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>865 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>126</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>2604 Aldrich in Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2020-09-22</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>September 2020</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>12 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175018</th>\n",
       "      <td>A849492</td>\n",
       "      <td>*Dill</td>\n",
       "      <td>7011 Millrace Drive in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Chihuahua Shorthair</td>\n",
       "      <td>01/10/2020</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2022-01-10</td>\n",
       "      <td>2022-01-14</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>4 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175023</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Owner Surrender</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2022-01-10</td>\n",
       "      <td>2021-12-23</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>-18 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175024</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>12041 Harris Branch Parkway in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>2 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2021-12-13</td>\n",
       "      <td>2021-12-23</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>10 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175025</th>\n",
       "      <td>A848504</td>\n",
       "      <td>Eros</td>\n",
       "      <td>124 W Anderson Ln in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>12/21/2019</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown/Brown</td>\n",
       "      <td>2021-12-21</td>\n",
       "      <td>2022-01-16</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>26 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175033</th>\n",
       "      <td>A848107</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>14402 Callan in Travis (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Shih Tzu</td>\n",
       "      <td>12/14/2010</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2021-12-14</td>\n",
       "      <td>2021-12-20</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>6 days</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>14150 rows × 20 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Animal ID   Name                              Found Location  \\\n",
       "28       A836850   <NA>          6111 Softwood Drive in Austin (TX)   \n",
       "38       A815227   Baby            12305 Zeller Lane in Austin (TX)   \n",
       "120      A772747  Lamar          Thaxton And Sassman in Austin (TX)   \n",
       "123      A772747  Lamar      1709 Colony Creek Drive in Austin (TX)   \n",
       "126      A772747  Lamar                 2604 Aldrich in Austin (TX)   \n",
       "...          ...    ...                                         ...   \n",
       "175018   A849492  *Dill          7011 Millrace Drive in Austin (TX)   \n",
       "175023   A848016  Honey                                 Austin (TX)   \n",
       "175024   A848016  Honey  12041 Harris Branch Parkway in Austin (TX)   \n",
       "175025   A848504   Eros            124 W Anderson Ln in Austin (TX)   \n",
       "175033   A848107   <NA>                 14402 Callan in Travis (TX)   \n",
       "\n",
       "            Intake Type Intake Condition Sex upon Intake Age upon Intake  \\\n",
       "28        Public Assist         Pregnant   Intact Female         4 years   \n",
       "38                Stray           Normal   Intact Female         1 month   \n",
       "120               Stray           Normal   Neutered Male          1 year   \n",
       "123               Stray           Normal     Intact Male        5 months   \n",
       "126       Public Assist           Normal   Neutered Male         2 years   \n",
       "...                 ...              ...             ...             ...   \n",
       "175018            Stray           Normal     Intact Male         2 years   \n",
       "175023  Owner Surrender           Normal   Spayed Female        3 months   \n",
       "175024            Stray           Normal   Intact Female        2 months   \n",
       "175025            Stray           Normal     Intact Male         2 years   \n",
       "175033            Stray           Normal   Spayed Female        11 years   \n",
       "\n",
       "                                 Breed Date of Birth     Outcome Type  \\\n",
       "28                            Pit Bull    06/15/2017         Transfer   \n",
       "38                     Norfolk Terrier    01/12/2020  Return to Owner   \n",
       "120     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "123     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "126     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "...                                ...           ...              ...   \n",
       "175018             Chihuahua Shorthair    01/10/2020         Transfer   \n",
       "175023             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175024             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175025                        Pit Bull    12/21/2019         Adoption   \n",
       "175033                        Shih Tzu    12/14/2010         Transfer   \n",
       "\n",
       "       Outcome Subtype Animal_Type Sex upon Outcome Age upon Outcome  \\\n",
       "28             Partner         Dog    Intact Female          4 years   \n",
       "38                 NaN         Dog    Intact Female          1 month   \n",
       "120                NaN         Dog    Neutered Male          2 years   \n",
       "123                NaN         Dog    Neutered Male          2 years   \n",
       "126                NaN         Dog    Neutered Male          2 years   \n",
       "...                ...         ...              ...              ...   \n",
       "175018         Partner         Dog      Intact Male          2 years   \n",
       "175023             NaN         Dog    Spayed Female         3 months   \n",
       "175024             NaN         Dog    Spayed Female         3 months   \n",
       "175025             NaN         Dog    Neutered Male          2 years   \n",
       "175033         Partner         Dog    Spayed Female         11 years   \n",
       "\n",
       "              Color Intake Date Outcome Date    Intake Month  Outcome Month  \\\n",
       "28       Blue/White  2021-06-15   2021-06-16       June 2021      June 2021   \n",
       "38      Brown/Cream  2020-03-12   2020-03-13      March 2020     March 2020   \n",
       "120           White  2019-01-07   2020-10-04    January 2019   October 2020   \n",
       "123           White  2018-05-23   2020-10-04        May 2018   October 2020   \n",
       "126           White  2020-09-22   2020-10-04  September 2020   October 2020   \n",
       "...             ...         ...          ...             ...            ...   \n",
       "175018        Brown  2022-01-10   2022-01-14    January 2022   January 2022   \n",
       "175023     Tricolor  2022-01-10   2021-12-23    January 2022  December 2021   \n",
       "175024     Tricolor  2021-12-13   2021-12-23   December 2021  December 2021   \n",
       "175025  Brown/Brown  2021-12-21   2022-01-16   December 2021   January 2022   \n",
       "175033        Brown  2021-12-14   2021-12-20   December 2021  December 2021   \n",
       "\n",
       "       Stay_Duration  \n",
       "28            1 days  \n",
       "38            1 days  \n",
       "120         636 days  \n",
       "123         865 days  \n",
       "126          12 days  \n",
       "...              ...  \n",
       "175018        4 days  \n",
       "175023      -18 days  \n",
       "175024       10 days  \n",
       "175025       26 days  \n",
       "175033        6 days  \n",
       "\n",
       "[14150 rows x 20 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Dog"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5f838ed",
   "metadata": {
    "papermill": {
     "duration": 0.069198,
     "end_time": "2024-10-11T19:10:41.849402",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.780204",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Decided to only look at Dogs from this part forward to do a time series plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "51ddf071",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:41.995018Z",
     "iopub.status.busy": "2024-10-11T19:10:41.993886Z",
     "iopub.status.idle": "2024-10-11T19:10:42.032737Z",
     "shell.execute_reply": "2024-10-11T19:10:42.033403Z",
     "shell.execute_reply.started": "2022-12-16T15:23:23.793052Z"
    },
    "papermill": {
     "duration": 0.115304,
     "end_time": "2024-10-11T19:10:42.033623",
     "exception": false,
     "start_time": "2024-10-11T19:10:41.918319",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "Only_Dogs_Intake = Dog.groupby('Intake Date').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c24ba539",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:42.183623Z",
     "iopub.status.busy": "2024-10-11T19:10:42.182474Z",
     "iopub.status.idle": "2024-10-11T19:10:42.187414Z",
     "shell.execute_reply": "2024-10-11T19:10:42.186625Z",
     "shell.execute_reply.started": "2022-12-16T15:23:25.00391Z"
    },
    "papermill": {
     "duration": 0.084401,
     "end_time": "2024-10-11T19:10:42.187589",
     "exception": false,
     "start_time": "2024-10-11T19:10:42.103188",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "Only_Dogs_Intake = Only_Dogs_Intake.drop(columns=['Animal ID', 'Name', 'Found Location', 'Intake Type',\n",
    "       'Intake Condition', 'Sex upon Intake', 'Age upon Intake', 'Breed',\n",
    "'Date of Birth', 'Outcome Type', 'Outcome Subtype', 'Sex upon Outcome', 'Age upon Outcome', 'Color',\n",
    "       'Outcome Date', 'Intake Month', 'Outcome Month'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4c214224",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:42.335241Z",
     "iopub.status.busy": "2024-10-11T19:10:42.334341Z",
     "iopub.status.idle": "2024-10-11T19:10:42.354528Z",
     "shell.execute_reply": "2024-10-11T19:10:42.353809Z",
     "shell.execute_reply.started": "2022-12-16T15:23:25.989888Z"
    },
    "papermill": {
     "duration": 0.097384,
     "end_time": "2024-10-11T19:10:42.354708",
     "exception": false,
     "start_time": "2024-10-11T19:10:42.257324",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Month</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Intake Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2013-10-08</th>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-07</th>\n",
       "      <td>2</td>\n",
       "      <td>11</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-08</th>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-24</th>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013-11-29</th>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-11</th>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-12</th>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-13</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-14</th>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-15</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1497 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Animal_Type  Month  Year\n",
       "Intake Date                          \n",
       "2013-10-08             1     10  2013\n",
       "2013-11-07             2     11  2013\n",
       "2013-11-08             1     11  2013\n",
       "2013-11-24             1     11  2013\n",
       "2013-11-29             1     11  2013\n",
       "...                  ...    ...   ...\n",
       "2022-01-11            15      1  2022\n",
       "2022-01-12            11      1  2022\n",
       "2022-01-13             5      1  2022\n",
       "2022-01-14             9      1  2022\n",
       "2022-01-15             2      1  2022\n",
       "\n",
       "[1497 rows x 3 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Only_Dogs_Intake['Month'] = Only_Dogs_Intake.index.month\n",
    "Only_Dogs_Intake['Year'] = Only_Dogs_Intake.index.year\n",
    "Only_Dogs_Intake = Only_Dogs_Intake.drop(columns=['Stay_Duration'])\n",
    "Only_Dogs_Intake"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c28fb3c3",
   "metadata": {
    "papermill": {
     "duration": 0.069847,
     "end_time": "2024-10-11T19:10:42.494835",
     "exception": false,
     "start_time": "2024-10-11T19:10:42.424988",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### Re-importing packages and creating a grid layout for time series plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4535c77b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:42.648514Z",
     "iopub.status.busy": "2024-10-11T19:10:42.647509Z",
     "iopub.status.idle": "2024-10-11T19:10:44.256607Z",
     "shell.execute_reply": "2024-10-11T19:10:44.255900Z",
     "shell.execute_reply.started": "2022-12-16T15:23:32.142901Z"
    },
    "papermill": {
     "duration": 1.690714,
     "end_time": "2024-10-11T19:10:44.256793",
     "exception": false,
     "start_time": "2024-10-11T19:10:42.566079",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.tsa.stattools import adfuller, kpss, acf, grangercausalitytests\n",
    "from statsmodels.graphics.tsaplots import plot_acf, plot_pacf,month_plot,quarter_plot\n",
    "from scipy import signal\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns \n",
    "%matplotlib inline \n",
    "sns.set_style(\"whitegrid\")\n",
    "plt.rc('xtick', labelsize=15) \n",
    "plt.rc('ytick', labelsize=15) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5b6d2fcb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:44.413902Z",
     "iopub.status.busy": "2024-10-11T19:10:44.403162Z",
     "iopub.status.idle": "2024-10-11T19:10:45.202900Z",
     "shell.execute_reply": "2024-10-11T19:10:45.203531Z",
     "shell.execute_reply.started": "2022-12-16T15:23:34.556067Z"
    },
    "papermill": {
     "duration": 0.874558,
     "end_time": "2024-10-11T19:10:45.203749",
     "exception": false,
     "start_time": "2024-10-11T19:10:44.329191",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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8gCk4nqJ1KPLaS1Pr28tc4GqqN1Btdm8W2+9VW/7bbfdhtzcXGRnZyMsLAxFRUVGxxYWFgIAwsLCXF1MIiIiIiJyBfYG9QiiBoExMTEW35dKpYiJicGVK1eM3ktKSkKLFi2s6gpKREREREREpokaBN55550AgAMHDuht379/PyIjI9G0aVOMHDkSWVlZOHr0qPB+SUkJ9uzZgxEjRohZXCIiIiIiciaJuwtAgMhjAocNG4YBAwZg3rx5KCgoECaGOXDgABYsWAAAGDFiBHr37o3Zs2djzpw5wmLxarUaU6dOFbO4RERERETkTOwO6hFEDQIlEgm++eYbfPLJJ/jyyy9RVFSEdu3a4eOPP8a9994LQNMldOnSpfjwww8xf/58yOVy9OrVC6tXr0ZUVJSYxSUiIiIiIidgAtCziBoEAkBISAjmzZuHefPmmd0nPDxcyAwSERERERGR84g6JpCIiIiIiIjci0EgERERERGJQs1BgR6BQSAREREREVE9wiCQiIiIiIhEIeEUMR6BQSAREREREYmC3UE9A4NAIiIiIiJyKYmEGUBPwiCQiIiIiIioHmEQSEREREREVI8wCCQiIiIiIlGoOSTQIzAIJCIiIiIiqkcYBBIRERERkSg4P4xnYBBIRERERESiYHdQz8AgkIiIiIiIqB5hEEhERERERFSPMAgkIiIiIiKX4lhAz8IgkIiIiIiIqB5hEEhERERERFSPMAgkIiIiIiKqRxgEEhERERGRKLhChGdgEEhERERERFSPMAgkIiIiIiKqRxgEEhERERGRS1laIUKuUIpWDtJgEEhERERERG6x+XQ6Or25A1ezS9xdlHqFQSAREREREbnF3xeyAACXbha5uST1C4NAIiIiIiJyC3X1fKESix1GydkYBBIRERERkSjUarXBa81/JYwBRcUgkIiIiIiI3EIIAt1bjHqHQSAREREREbmF0B2UUaCoGAQSEREREZFLmQvyanqHMgoUE4NAIiIiIiJyKYOhgDXbq//LTKC4GAQSEREREZFbcEygezAIJCIiIiIilzKf6dOOCWQYKCYGgUREREREJArDXqHMBLoHg0AiIiIiInILjgl0DwaBRERERETkFtrF4xkEiotBIBERERERuZjpKE/IBLJDqKgYBBIRERERkYuZXiNCXRMFkoh8xb7gkSNHMHHiRKPtoaGhOH78uPBa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g4iIiIiIqE7xyEwgERERERERuQaDQCIiIiIionpEolar1e4uhCucPn0a/v7+7i4GERERERGRW8jlcvTq1ctoe50NAomIiIiIiMgYu4MSERERERHVIwwCiYiIiIiI6hEGgURERERERPUIg0AiIiIiIqJ6hEEgERERERFRPeLr7gLUVzt27MDWrVtx/vx55OXlISoqCqNGjcKzzz6LkJAQYT+ZTIZFixZh165dwhSvr732Gjp16qR3vk8//RTnz5/HhQsXUFhYiAULFuChhx6yWIaTJ0/i0UcfhVqtxoULF+DrW3cfB3fV9xNPPIGjR48abX/ttdfw5JNPOv0+PYU7n2+ZTIavvvoKO3fuRG5uLiIiInDrrbdi4cKFLr1nd3JHfR85cgQTJ040W6Z169aZnJK6LnDX811eXo7vvvsOW7duRWZmJho1aoQBAwbg+eefR3R0tMvv213cWd+fffYZtm/fjoKCArRr1w5PP/007rvvPpffszs5s77PnTuH9evX49ixY8Iz27dvX7z44oto1aqV3nVVKhW+++47rFu3Djk5OWjXrh2ee+453HXXXaLduzu4q75XrFiBI0eO4Pz588jJycHMmTMxa9Ys0e7bXdxR39evX8eaNWtw5MgRpKWlITg4GN26dcOLL76Izp07i3r/urhEhJtMmDABUVFRGDlyJCIjI3Hx4kV89dVXaN++PX755RdIpVKo1Wo8+uijSE9Px5w5cxAWFoZly5bhypUr2Lx5MyIjI4Xz9e7dG3FxcWjVqhU2bdpUaxBYVVWFhx56CAUFBcjJyanzQaC76vuJJ56ATCbDO++8o7e9ZcuWaNq0qcvv213cVd8ymQyPPvooJBIJpk6dipYtWyI7OxsnT57EW2+9JWYViMod9V1SUoKrV68aleWNN96ATCbD3r174ePj4/J7dwd3Pd+vvPIKdu3ahVmzZqFbt27IzMzEl19+CalUis2bNyM4OFjMahCNu+p7ypQpOH36NF588UW0a9cOf//9N9atW4dFixbh/vvvF7MKROXM+v7www9x6tQp3HvvvejYsSOysrLwzTffID8/H5s2bUJUVJRw3c8++wzLly/HSy+9hK5du2Lbtm1Yv349vv32WwwbNsxd1eFy7qrv0aNHIyQkBF26dMEvv/xSb4JAd9T3Tz/9hHXr1uHBBx9Ely5dUFxcjO+//x4JCQn4+eef0a1bN/dUhprcIi8vz2jb77//ro6NjVX/+++/arVard65c6c6NjZWfejQIWGfoqIidb9+/dTvvvuu3rFKpVKtVqvVycnJ6tjYWPWvv/5q8fpLlixRjxkzRv3pp5+qY2Nj1VVVVY7ekkdzV30//vjj6v/85z/Oug2v4a76fuutt9S33367uri42Fm34hXc/fdEKy0tTd2pUyf1woUL7b0Vr+CO+i4rK1PHxcWpP/nkE73te/fuVcfGxqr37dvn8H15KnfU97Fjx0y+98wzz6gHDx6sVigUDt+Xp3JmfZs6l/bvxOeffy5sy83NVXft2lX9xRdf6O07ceJE9dixYx2+J0/mjvpWq2t+D6qqqtSxsbHqxYsXO+V+PJ076jsvL0+tUqn09isqKlLfcsst6tmzZzt8T/bimEA3iYiIMNrWvXt3AEBWVhYAYPfu3WjWrBkGDhwo7BMaGorhw4cjPj5e71ip1PqPMiUlBUuWLMG8efPqdPZPlzvruz5yR32XlZVh8+bNePjhh/W6dNQHnvJ8b968GWq1Gg8++KBdx3sLd9S3UqmEUqk0erbDwsIAaLrS1VXuqO8zZ84AAIYOHaq3fciQIcjJycHp06dtugdv4sz6NnWuli1bIiIiQjgXAOzfvx9VVVVGXW3vu+8+XL58GampqY7dlAdzR30D9bcd4476joiIgEQi0dsvNDQUbdu2NfpcxFQ/nwAPpR071qFDBwDA1atXERsba7RfTEwMMjIyUFpaatd15s2bh7vvvhv9+vWzv7B1gFj1nZCQgL59+6Jr16649957sWHDBvsL7cVcXd8XLlxARUUFmjRpgueffx49evRA7969MWPGjDrdgDBHrOdb1+bNm9G1a1eT16nrXF3fISEhuP/++7F69WocPnwYpaWluHLlChYtWoTOnTtj0KBBjt+EF3F1fWu7Mvv5+eltb9CgAQDgypUrNpfZmzmzvpOSkpCXlyecS3u+Bg0aoE2bNnr7duzYUTimPnF1fZM+d9R3YWEhrly54tbPhUGgh8jKysLixYtx6623Ct9IyGQy4VteXeHh4QCAoqIim6+zefNmXLhwAXPmzHGovN5OrPq+5ZZb8Prrr2PJkiX44osv0LZtW7z55pv45ptvHCq/txGjvrOzswFo+uhLpVIsWbIE77zzDhISEjBx4kSUlJQ4dhNeRKznW9epU6eQnJyMBx54wKHzeCOx6nvBggW48847MWnSJPTp0wdjx46FQqHAihUrhOCkPhCjvtu1awcARhm/U6dOCderL5xZ3wqFAvPmzUNERAQefvhhYbv2fIbZkoYNGwLQNJjrCzHqm2q4q77fffddqNVqTJo0ybEbcED96Avo4UpLSzF9+nT4+PhgwYIFLrtOYWEhFi5ciJdeegmNGzd22XU8nVj1DQAvvPCC3us77rgDzz33HJYuXYpJkybV2YkcdIlV39rucK1atcJnn30mNCZat26NCRMmYMuWLXj00Udddn1PIebzrev333+Hn58fxo4dK9o1PYGY9f35559jy5Yt+N///ofu3bsjIyMDX3/9NaZOnYqffvoJQUFBLr2+JxCrvgcPHowOHTrg/fffR1hYGNq3b4+///4bW7duBQCjYKWucnZ9v/POOzh16hS+/fZbIcCjGqxvcbmrvr/99lv8+eefeP/9942y32JiJtDNKioqMG3aNKSlpWH58uV6M5iFhYWZ/LZB+42YqW8pLPn888/RtGlTjB49GkVFRSgqKoJcLgcAFBcXo6yszP4b8RJi1rc5Y8aMgVwux+XLl51yPk8mZn1rv6EbNGiQXgOtZ8+eCAkJQUJCgu034GXc9XxXVlZix44dGDZsmMkxEnWVmPV95coVLFu2DHPnzsXkyZPRr18/3H///Vi2bBkuXLhQL7qZi1nfvr6+WLx4MQIDA/Gf//wH/fv3x+eff46XX34ZANCsWTP7b8RLOLu+P/74Y6xfvx7vv/8+brvtNr33tOdTG0xYr824av++12Vi1je5r77Xrl2LTz/9FC+++KLbs7PMBLpRVVUVnn/+eZw/fx4rVqwwWssoJiYGBw8eNDouKSkJLVq0sDmLlJSUhMTERAwYMMDovYEDB2LkyJF1upui2PVdm7r+TbLY9a0dO2IO69t1z3d8fDxkMlmdnxBGl9j1rf3SSNtdSatt27YICwur82Om3PF8x8TEYPPmzUhLS0N5eTnatm2LnTt3AgD69Olj3414CWfX95IlS/Ddd9/hrbfeMtllvGPHjqisrERKSopeZkS7DE1dH88mdn3Xd+6q702bNmH+/PmYPHkypk+f7pR7cQQzgW6iUqnw6quv4vDhw/jmm29MLqo8cuRIZGVl6S02XlJSgj179mDEiBE2X/P111/H6tWr9f6nbbStXLkSL774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\n",
      "text/plain": [
       "<Figure size 1080x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "### create a 'Over Time Plot'\n",
    "fig, ax = plt.subplots(figsize=(15,6))\n",
    "sns.lineplot(x=Only_Dogs_Intake.index, y=Only_Dogs_Intake['Animal_Type'])\n",
    "ax.set_title('# of Dogs Taken in Over Time', fontsize = 20, loc='center', fontdict=dict(weight='bold'))\n",
    "ax.set_xlabel('Year', fontsize = 16, fontdict=dict(weight='bold'))\n",
    "ax.set_ylabel('Count', fontsize = 16, fontdict=dict(weight='bold'))\n",
    "plt.tick_params(axis='y', which='major', labelsize=16)\n",
    "plt.tick_params(axis='x', which='major', labelsize=16)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "cd3f9e1f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:45.360081Z",
     "iopub.status.busy": "2024-10-11T19:10:45.359171Z",
     "iopub.status.idle": "2024-10-11T19:10:45.827962Z",
     "shell.execute_reply": "2024-10-11T19:10:45.827301Z",
     "shell.execute_reply.started": "2022-12-16T15:23:44.214612Z"
    },
    "papermill": {
     "duration": 0.549801,
     "end_time": "2024-10-11T19:10:45.828172",
     "exception": false,
     "start_time": "2024-10-11T19:10:45.278371",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Year'>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Only_Dogs_Intake.groupby('Year').Animal_Type.count().plot.bar()\n",
    "##It's clear the pandemic boosted the number of dogs being taken in."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "25c7e367",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:46.013519Z",
     "iopub.status.busy": "2024-10-11T19:10:46.009855Z",
     "iopub.status.idle": "2024-10-11T19:10:49.998042Z",
     "shell.execute_reply": "2024-10-11T19:10:49.998723Z",
     "shell.execute_reply.started": "2022-12-16T15:23:54.825705Z"
    },
    "papermill": {
     "duration": 4.095794,
     "end_time": "2024-10-11T19:10:49.998937",
     "exception": false,
     "start_time": "2024-10-11T19:10:45.903143",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Count of Dogs')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Create Seasonality Plot\n",
    "fig, ax = plt.subplots(figsize=(15,6))\n",
    "palette = sns.color_palette(\"ch:2.5,-.2,dark=.3\", 10)\n",
    "sns.lineplot(x= Only_Dogs_Intake['Month'], y=Only_Dogs_Intake['Animal_Type'], hue=Only_Dogs_Intake['Year'], palette=palette)\n",
    "ax.set_title('Seasonal Plot of Intake Date for Austin Shelter Dogs', fontsize=20, loc='center', fontdict=dict(weight='bold'))\n",
    "ax.set_xlabel('Month', fontsize=16, fontdict=dict(weight='bold'))\n",
    "ax.set_ylabel('Count of Dogs', fontsize=16, fontdict=dict(weight='bold'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9fa83884",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:50.177304Z",
     "iopub.status.busy": "2024-10-11T19:10:50.165346Z",
     "iopub.status.idle": "2024-10-11T19:10:51.096586Z",
     "shell.execute_reply": "2024-10-11T19:10:51.095897Z",
     "shell.execute_reply.started": "2022-12-16T15:24:04.397165Z"
    },
    "papermill": {
     "duration": 1.019282,
     "end_time": "2024-10-11T19:10:51.096763",
     "exception": false,
     "start_time": "2024-10-11T19:10:50.077481",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Count of Dogs')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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DHLe3t6MHj0agP3795OVlcWNGzcwm80cP36czZs3s2HDBqBnh+To6IiDgwPHjh1j//79AxG6iIhIn4WGhhIUFERQUBChoaG9luneJx48eJD8/Hxu3LjB3r17OXXqFNA5Onfn7Z99NWbMGAAaGxu5dOlSv+oQGew0B1BkkHNyciIxMZGVK1fS3t7OihUrLMp0LdoSEBCAg4MDra2t7Nmzhz179gDw8MMP09jYaNO4RURE/hf3338/KSkpf1nGycmJhIQEPvjgA9rb2y1Wtx4xYoSxIEx/PP7445SXl2M2m5kxYwbQ2cdu2rSp33WKDDYaART5PxASEsLXX39NcHAw48aNw87ODpPJhJeXF9HR0cYtnhMmTOCzzz7j0UcfxcHBAVdXV9asWUNISMgAvwMREZF7Y/78+ezatYuZM2cyZswY7OzsGDduHHPnzuWbb77Bz8+v33XHxMTw3HPPYTKZ7mHEIoPLsI6Ojo6BDkJERERERESsTyOAIiIiIiIiQ4QSQBERERERkSFCCaCIiIiIiMgQoQRQRERERERkiFACKCIiIiIiMkQoARQRERERERkilACKiIiIiIgMEUoARUREREREhgglgCIiIiIiIkPEfwCKh/vS7pQ8iAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x432 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))\n",
    "sns.boxplot(x=Only_Dogs_Intake['Year'], y=Only_Dogs_Intake['Animal_Type'], ax=ax[0])\n",
    "ax[0].set_title('Year-wise Box Plot\\n(The Trend)', fontsize = 20, loc='center', fontdict=dict(weight='bold'))\n",
    "ax[0].set_xlabel('Year', fontsize = 16, fontdict=dict(weight='bold'))\n",
    "ax[0].set_ylabel('Count of Dogs', fontsize = 16, fontdict=dict(weight='bold'))\n",
    "sns.boxplot(x=Only_Dogs_Intake['Month'], y=Only_Dogs_Intake['Animal_Type'], ax=ax[1])\n",
    "ax[1].set_title('Month-wise Box Plot\\n(The Seasonality)', fontsize = 20, loc='center', fontdict=dict(weight='bold'))\n",
    "ax[1].set_xlabel('Month', fontsize = 16, fontdict=dict(weight='bold'))\n",
    "ax[1].set_ylabel('Count of Dogs', fontsize = 16, fontdict=dict(weight='bold'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17f6db22",
   "metadata": {
    "papermill": {
     "duration": 0.083423,
     "end_time": "2024-10-11T19:10:51.262223",
     "exception": false,
     "start_time": "2024-10-11T19:10:51.178800",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "2021 is the most standout INTAKE year and the months of March, June, and September have the highest count of dogs taken in, demonstrating that a beginning of the season is a good time for many dogs to be abandoned or found."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c27c1e99",
   "metadata": {
    "papermill": {
     "duration": 0.080678,
     "end_time": "2024-10-11T19:10:51.424737",
     "exception": false,
     "start_time": "2024-10-11T19:10:51.344059",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Let's Look at Outcome Now"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "18a4b493",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:51.598375Z",
     "iopub.status.busy": "2024-10-11T19:10:51.595480Z",
     "iopub.status.idle": "2024-10-11T19:10:51.635739Z",
     "shell.execute_reply": "2024-10-11T19:10:51.634932Z",
     "shell.execute_reply.started": "2022-12-16T15:24:20.938527Z"
    },
    "papermill": {
     "duration": 0.12905,
     "end_time": "2024-10-11T19:10:51.635944",
     "exception": false,
     "start_time": "2024-10-11T19:10:51.506894",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Let's look at outcome\n",
    "Dogs_Outcome= Dog.groupby('Outcome Date').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d0b0ee59",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:51.810424Z",
     "iopub.status.busy": "2024-10-11T19:10:51.809096Z",
     "iopub.status.idle": "2024-10-11T19:10:51.817928Z",
     "shell.execute_reply": "2024-10-11T19:10:51.817196Z",
     "shell.execute_reply.started": "2022-12-16T15:24:23.41921Z"
    },
    "papermill": {
     "duration": 0.100644,
     "end_time": "2024-10-11T19:10:51.818117",
     "exception": false,
     "start_time": "2024-10-11T19:10:51.717473",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "Dogs_Outcome = Dogs_Outcome.drop(columns=['Animal ID', 'Name', 'Found Location', 'Intake Type',\n",
    "       'Intake Condition', 'Sex upon Intake', 'Age upon Intake', 'Breed', 'Intake Date', 'Stay_Duration','Date of Birth', 'Outcome Type', 'Outcome Subtype', 'Sex upon Outcome', 'Age upon Outcome', 'Color',\n",
    "        'Intake Month', 'Outcome Month'])\n",
    "Dogs_Outcome['Month'] = Dogs_Outcome.index.month\n",
    "Dogs_Outcome['Year'] = Dogs_Outcome.index.year\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "62d225b6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:52.009031Z",
     "iopub.status.busy": "2024-10-11T19:10:52.008193Z",
     "iopub.status.idle": "2024-10-11T19:10:52.224778Z",
     "shell.execute_reply": "2024-10-11T19:10:52.223910Z",
     "shell.execute_reply.started": "2022-12-16T15:24:24.664787Z"
    },
    "papermill": {
     "duration": 0.326426,
     "end_time": "2024-10-11T19:10:52.224956",
     "exception": false,
     "start_time": "2024-10-11T19:10:51.898530",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Year'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Dogs_Outcome.groupby('Year').Animal_Type.mean().plot.bar()\n",
    "### Outcome Date shows the influence of the pandemic"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06c39eba",
   "metadata": {
    "papermill": {
     "duration": 0.081648,
     "end_time": "2024-10-11T19:10:52.389240",
     "exception": false,
     "start_time": "2024-10-11T19:10:52.307592",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Linear Regression will be used"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8e2e9b8b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:52.561182Z",
     "iopub.status.busy": "2024-10-11T19:10:52.560247Z",
     "iopub.status.idle": "2024-10-11T19:10:52.589068Z",
     "shell.execute_reply": "2024-10-11T19:10:52.588436Z",
     "shell.execute_reply.started": "2022-12-16T15:24:29.916558Z"
    },
    "papermill": {
     "duration": 0.118597,
     "end_time": "2024-10-11T19:10:52.589311",
     "exception": false,
     "start_time": "2024-10-11T19:10:52.470714",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Month</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-03-31</th>\n",
       "      <td>828</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-04-30</th>\n",
       "      <td>359</td>\n",
       "      <td>4</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-05-31</th>\n",
       "      <td>379</td>\n",
       "      <td>5</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-30</th>\n",
       "      <td>490</td>\n",
       "      <td>6</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-07-31</th>\n",
       "      <td>458</td>\n",
       "      <td>7</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-31</th>\n",
       "      <td>513</td>\n",
       "      <td>8</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-09-30</th>\n",
       "      <td>564</td>\n",
       "      <td>9</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-10-31</th>\n",
       "      <td>603</td>\n",
       "      <td>10</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-11-30</th>\n",
       "      <td>535</td>\n",
       "      <td>11</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-12-31</th>\n",
       "      <td>587</td>\n",
       "      <td>12</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-31</th>\n",
       "      <td>532</td>\n",
       "      <td>1</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-02-28</th>\n",
       "      <td>402</td>\n",
       "      <td>2</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-03-31</th>\n",
       "      <td>591</td>\n",
       "      <td>3</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-30</th>\n",
       "      <td>556</td>\n",
       "      <td>4</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-05-31</th>\n",
       "      <td>709</td>\n",
       "      <td>5</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-06-30</th>\n",
       "      <td>839</td>\n",
       "      <td>6</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-07-31</th>\n",
       "      <td>877</td>\n",
       "      <td>7</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-08-31</th>\n",
       "      <td>802</td>\n",
       "      <td>8</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-09-30</th>\n",
       "      <td>834</td>\n",
       "      <td>9</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-10-31</th>\n",
       "      <td>734</td>\n",
       "      <td>10</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-11-30</th>\n",
       "      <td>749</td>\n",
       "      <td>11</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-12-31</th>\n",
       "      <td>815</td>\n",
       "      <td>12</td>\n",
       "      <td>2021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-01-31</th>\n",
       "      <td>394</td>\n",
       "      <td>1</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Animal_Type  Month  Year\n",
       "Outcome Date                          \n",
       "2020-03-31            828      3  2020\n",
       "2020-04-30            359      4  2020\n",
       "2020-05-31            379      5  2020\n",
       "2020-06-30            490      6  2020\n",
       "2020-07-31            458      7  2020\n",
       "2020-08-31            513      8  2020\n",
       "2020-09-30            564      9  2020\n",
       "2020-10-31            603     10  2020\n",
       "2020-11-30            535     11  2020\n",
       "2020-12-31            587     12  2020\n",
       "2021-01-31            532      1  2021\n",
       "2021-02-28            402      2  2021\n",
       "2021-03-31            591      3  2021\n",
       "2021-04-30            556      4  2021\n",
       "2021-05-31            709      5  2021\n",
       "2021-06-30            839      6  2021\n",
       "2021-07-31            877      7  2021\n",
       "2021-08-31            802      8  2021\n",
       "2021-09-30            834      9  2021\n",
       "2021-10-31            734     10  2021\n",
       "2021-11-30            749     11  2021\n",
       "2021-12-31            815     12  2021\n",
       "2022-01-31            394      1  2022"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monthly = Dogs_Outcome.resample('M').sum()\n",
    "monthly['Month'] = monthly.index.month\n",
    "monthly['Year'] = monthly.index.year\n",
    "monthly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2f35acde",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:52.770964Z",
     "iopub.status.busy": "2024-10-11T19:10:52.770013Z",
     "iopub.status.idle": "2024-10-11T19:10:52.774920Z",
     "shell.execute_reply": "2024-10-11T19:10:52.774183Z",
     "shell.execute_reply.started": "2022-12-16T15:24:31.580002Z"
    },
    "papermill": {
     "duration": 0.103173,
     "end_time": "2024-10-11T19:10:52.775093",
     "exception": false,
     "start_time": "2024-10-11T19:10:52.671920",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Month</th>\n",
       "      <th>Year</th>\n",
       "      <th>Time Step</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-03-31</th>\n",
       "      <td>828</td>\n",
       "      <td>3</td>\n",
       "      <td>2020</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-04-30</th>\n",
       "      <td>359</td>\n",
       "      <td>4</td>\n",
       "      <td>2020</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-05-31</th>\n",
       "      <td>379</td>\n",
       "      <td>5</td>\n",
       "      <td>2020</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-30</th>\n",
       "      <td>490</td>\n",
       "      <td>6</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-07-31</th>\n",
       "      <td>458</td>\n",
       "      <td>7</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Animal_Type  Month  Year  Time Step\n",
       "Outcome Date                                     \n",
       "2020-03-31            828      3  2020          0\n",
       "2020-04-30            359      4  2020          1\n",
       "2020-05-31            379      5  2020          2\n",
       "2020-06-30            490      6  2020          3\n",
       "2020-07-31            458      7  2020          4"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monthly['Time Step'] = np.arange(len(monthly.index))\n",
    "monthly.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7ddb5fbd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:52.950958Z",
     "iopub.status.busy": "2024-10-11T19:10:52.949866Z",
     "iopub.status.idle": "2024-10-11T19:10:52.954459Z",
     "shell.execute_reply": "2024-10-11T19:10:52.953631Z",
     "shell.execute_reply.started": "2022-12-16T15:24:33.650972Z"
    },
    "papermill": {
     "duration": 0.095678,
     "end_time": "2024-10-11T19:10:52.954648",
     "exception": false,
     "start_time": "2024-10-11T19:10:52.858970",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Animal_Type    int64\n",
       "Month          int64\n",
       "Year           int64\n",
       "Time Step      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monthly.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ed02b102",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:53.136583Z",
     "iopub.status.busy": "2024-10-11T19:10:53.131032Z",
     "iopub.status.idle": "2024-10-11T19:10:53.809973Z",
     "shell.execute_reply": "2024-10-11T19:10:53.810631Z",
     "shell.execute_reply.started": "2022-12-16T15:24:34.822623Z"
    },
    "papermill": {
     "duration": 0.772178,
     "end_time": "2024-10-11T19:10:53.810847",
     "exception": false,
     "start_time": "2024-10-11T19:10:53.038669",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'TIme Plot of Dogs Only Outcome')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABiEAAAIxCAYAAAArGBueAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAABYlAAAWJQFJUiTwAAEAAElEQVR4nOzdeXxU9bk/8M+ZNbNkm+wrWSCQsAUQEXcrbiiyWEUUW61t7aVal7ZXba/W2ip6q7buVttb1/anIqBVBEQrrigCSQgEEgghK9m32Zdzfn+EHDLMTEhgJpNMPu/XixdzlvmeZyaTk+Q85/s8giRJEoiIiIiIiIiIiIiIiIJMEe4AiIiIiIiIiIiIiIgoMjEJQUREREREREREREREIcEkBBERERERERERERERhQSTEEREREREREREREREFBJMQhARERERERERERERUUgwCUFERERERERERERERCHBJAQREREREREREREREYUEkxBERERERERERERERBQSTEIQEREREREREREREVFIMAlBREREREREREREREQhwSQEERERERERERERERGFBJMQREREREREREREREQUEkxCEBERERERERERERFRSKjCHQARERERRaZvvvkGP/jBD3zWr169GsuWLQtDRGObKIrYuHEjNm7ciIqKCrS1tcFms0GSJHmf008/Ha+99loYoyTyxvMAERERETEJQURERCPie9/7HhoaGoI65tKlS/HII48AANauXYt777130H3I19NPP41nnnnmhPsJggCj0YjY2FhMmjQJs2fPxqJFi5CWljYCUZ6atWvX+nz2oqOjceONN4YnoJNgNptxyy234LvvvgvJ+IN9DpRKJVQqFTQaDWJiYhAXF4f09HTk5uZi5syZOOuss6DT6UISF/mqr6/H1q1bsX37dlRVVaGrqwvd3d3QarWIjY1FcnIyZs+ejXnz5uGss86CSsU/+U7VWHzPt2zZgoqKCp/1t912WxiiISIiovEu/L8dEREREdGoJ0kSent70dvbi/r6evznP//Bn//8Z1x99dX49a9/jejo6HCHGNC6devw7bffeq3LyMgYU0mIJ554ImQJiBPxeDzweDxwOBzo7e1FQ0MD9uzZI2/X6/VYsmQJfvaznyElJSUsMY4HBw8exLPPPouNGzfC4/H4bHe5XDCbzWhoaMCuXbvw97//HRkZGbj55puxYsUKKBSsxDtcY/k937JlC9atW+eznkkIIiIiCgf+JkpEREREJ0UURbz55ptYuXIluru7wx1OxBJFEf/+97/DHUZAVqsV//znP7Fw4cJRHedYtn79elx11VX44IMP/F4MD6ShoQEPPvggbrrpJrS3t4cwwsjD95yIiIgoeJiEICIiIqJTsm/fPtx3333hDiNidXR0oKenx2f9zJkzsWnTJuzevRt79uzBnj178PLLL498gEeZzWb86le/CmsMkei1117D3XffDZvNdtJjbNu2Dddddx2ThUPE95yIiIgouFiOiYiIiEbERx995NVAd6DGxkZcdNFFPuszMjKwefPmgGOyvEjorFq1Cj//+c/l5dbWVuzatQuPP/446uvrffbftGkT9u7di6KiopEMc1yw2+1+15999tnIyckJ6bH7PweSJMFsNqO1tRWlpaVYv359wPJQjz76KDIzM7FgwYKQxjYefP3111i9erXfbbGxsfjxj3+MCy+8EKmpqbDZbNizZw9ee+01fP755z7719TU4Pbbb8c//vEPCIIQ6tDHLL7nRERERMHHJAQRERGNCKVSGXDbYMmEUDX4vOGGG/z2Cfjkk0/gcrnw9ttv4/3338fBgwfhdDrli6orV65EQkKC/ByPx4MPP/wQa9asQVVVFXp6epCUlIS5c+fipptuwpQpU4YcU2lpKTZv3owdO3agoaEB3d3dUCqVMJlMmDp1Ks455xxceeWV0Gq1QXsfAlEoFF7vfVpaGtLS0jBz5kxcccUVsFqtPs/5+OOPg5aEqK2txXvvvYedO3fi0KFD6OrqgsvlQlxcHFJTUzF79mwsWLAAp59+ut/nn6jhdkNDAyZPnuyzPliNzO12Oz744AN8/fXXKC8vR2dnJ8xmMwwGA+Lj4zFt2jScccYZuOKKKwI2dT5RM/dnn30Wzz77rNe6V199FfPmzTvl+PsN/BzEx8cjPj4eBQUFuPrqq/Hxxx/jnnvu8ZmlIYoifvvb3+KMM86A0WgcdPxT/Tr7U19fj9dffx1bt25FU1MT1Go10tPT8b3vfQ8rVqxAcnJywEb2g71/u3fvxoYNG1BaWora2lqYzWY4nU5otVrEx8cjPT0dEydOxNSpU3HaaachNzd3yDH7I4oi/vjHP/otBZSdnY3XXnsNqamp8jqDwYDzzjsP5513Hp577jk8+eSTPs/7+uuv8eGHH2LhwoU+2wb7fnC73Vi3bh0+/PBDVFZWoqurCzExMZg+fTquvvrqU0447dy5EytWrPBZ/9hjj2HRokUBn7dlyxavZGm/l19+GfPnzx92HCP5ntfX1+PCCy/02f/WW2/127dhKPsH+lwP5O/rfPrpp+O1117zu78oiti6dSs+//xzlJSUoKWlBd3d3ZAkCXFxccjOzsb06dNx5plnYv78+dBoNAGPHYzzYj9/58f+12GxWPDGG29g06ZNOHz4MCRJQnZ2Nq644gosX77c67zkcDiwfv16rFu3DocOHYLdbkdKSgrOPPNM3HzzzcjKyho0joG++uorfPLJJ9i5cydaWlrQ1dUFrVaLhIQEzJw5ExdccAEuueSSQX8fIiIiilRMQhAREREN0NjYiFWrVqGiosJrfWVlJSorK/H222/jr3/9K6ZOnYr29nbceeed+Oabb7z2bWhoQENDA9577z088MADWL58+aDHrKmpwX333eeTFOlntVpRX1+PTZs24emnn8b9998ftrvMMzIycN555+HDDz/02VZdXX3K43d3d+PBBx/Ehg0bIIqiz/bW1la0trZi9+7deOWVVzBjxgw89NBDKCgoOOVjB8u//vUvPPnkk+js7PTZ1t3dje7ubtTU1OD999/HY489httvvx3XXXddGCI9NRdeeCGeffZZ3HTTTXC73V7burq68I9//CNgE9xQfZ3XrVuH3//+915ldGw2G3p6erBv3z688cYbePjhh4f1Ou12O37729/i/fff97vdarXCarWioaEB27dvl9c/99xzfi8aD9XGjRtx4MABn/VKpRJ/+ctfvC6GH2/VqlUoKyvDf/7zH59tzz77rN8kRCCVlZW46667UFVV5bW+vb0dn376KT799FMsWbIEDz/88ElfXJ09ezamTp3q1fAcAN5+++1BkxAbN270WZeeno4zzjjjpOIYLe/5aPHxxx9j9erVqKur87u9//t0x44dePnll/Hss88G/Nk0UufFffv24ec//7nPjL29e/di7969WLNmDV588UVkZWWhtrYWt912G/bt2+e17+HDh3H48GGsXbsWTz75JC644IJBj1lWVob77rvPZxzgWPPyw4cP47333kNubi4eeughzJkzZ9ivjYiIaCxjDQMiIiKio6xWK2666SafBMRAra2t+NnPfoa2tjb85Cc/8UlADCSKIh544AGUlJQE3Oerr77CsmXLAiYgjtfc3Ixbb70Vr7zyypD2D4X09HS/60+19nldXR2WLl2K999/3++FaX/Kyspw9dVX+73wN9IkScLdd9+NBx54wO+FNn+6urrw+9//Hvfcc0/AcmWj2emnn46rrrrK77Z169b5XR+qr/O7776Le++9d9A6/t3d3bj99tvx6aefDum4APDAAw8ETEAM5lS/nps2bfK7/nvf+x6mTp16wuf/4he/8Lv+wIEDOHjw4JBiqKysxMqVK30SEMdbv349/vGPfwxpzECuv/56n3Xffvstamtr/e7vdDr9fh4WL1580qWPRsN7Plo89thjWLVqVcAExFCN5HmxubkZP/rRj/yWDOxXXV2N2267DS0tLfjhD3/oN3HQz+Fw4K677hr0PXj33Xdx3XXXDTrOQIcOHcIPf/hDvwk0IiKiSMYkBBEREdFRnZ2dqKmpOeF+LS0tWLRokc9du/6IohiwLNDBgwdx2223wWKxDCtOSZLwyCOP+K1BPhIClQiKjY096TEtFgtuueWWQcsPBWK323HXXXdh//79J338YHjyySexfv36k3ruunXr8NRTTwU3oBES6G7lhoYGHDp0yGtdqL7O9fX1eOCBB4Z0wdLtdge82Hy85ubmk/6angpJkgImOC+55JIhjVFUVITs7Gy/27766qshjbFnz54hJxdffPFFOByOIe3rzxVXXIG4uDivdZIkYc2aNX73//zzz2E2m33WL1u27KSOP1re89HgH//4B1566aWgjDWS58XDhw+jvb39hPtVVFRg8eLFaGxsPOG+VqsVf/vb3/xu+/bbb/Hb3/4WLpdryDECfbMj7r777iEnLoiIiCIBkxBEREREx1m+fDk+/vhjfP3117jnnnv87tPR0QGg707wd999F9999x2eeuop6PV6n32//PJLvxfLVq9e7Xf9BRdcgDfeeAPffPMNtm7dioceeggmk8lrH1EU8fvf/96nDE6o1dfX47PPPvO77VRq4L/88st+7xSOj4/Hww8/jK+//lou+VFYWOizn9Vq9erl8POf/xx79uzBnj17MHfuXJ/9MzIy5O0D/w23VE+/urq6gBeqrrvuOmzYsAElJSXYuHEjVq5c6Xe/l156yeuO248++gh79uzBRx995Hf/VatW+cQ/nN4JwTJ58uSACajjZxUF++vc78UXX/Tbp8RkMuGxxx7D9u3bsW3bNjz88MOIiYkZ6kvD7t27fRIbOp0ODz74ID799FOUlpbiu+++w6ZNm/D888/jZz/7GWbOnHnKTYjb2toC3jU+lDvyT7Svv5JDg1mxYgU2bdqEnTt34vnnn0d0dLTPPt3d3fj666+HNe5AWq0WV199tc/6tWvX+j3P+SsJN2fOnIBJgBMZbe/5yVi6dKl8LliyZInfffyd915++WV5e3NzM/7yl7/4fW5GRgYefPBBbNmyBaWlpfj666/x8ssv44YbbvDb/yUU58WhWLVqFT7//HN88cUX+NGPfuR3n/6f4Zdccgk+/PBDfPvtt3jwwQf99qHyl7QURREPPvig3wTEsmXLsGbNGnz33XfYsmUL7rnnHp/fDex2O/7whz8M63URERGNZUxCEBEREQ1w/vnn48EHH0RmZiZMJhNuuukmTJ8+3e++aWlpeOGFFzBlyhRER0fjkksu8XtXuCiKPnc8HjhwwO9MhoULF+L555/HaaedJjfn/f73v4/nnnvO58JmXV0dNm/efAqvNjBRFOF2u+V/R44cwYYNG3DjjTf6vdgL4KTr34ui6LcpqkKhwIsvvoirrroKJpMJRqMR8+fPx6uvvoqUlBSf/b/66iv5Lvn+hsoqlSrgBeH+7QP/DdYkfTCvv/6634tRK1euxO9+9zvk5+dDp9MhNzcX9913n9/SMy6XC2+88Ya8rFQqB41p4Gs80WsNJUEQ/H49AHhd1A3F1xnoK8vz3nvv+R33r3/9KxYtWoSYmBjEx8fjqquuGtad1Xa73Wfd/PnzsXz5cqSlpSEqKgrR0dHIycnB9773Pdx5551466238MknnwQ8bwzFYGVrkpOThzxOoH2HWhYH6EvKPvDAA8jJyYHBYMD3vvc9/O53v/O77969e4c8rj/XXXedT1+J1tZWn/JZgUoxLV269KSPPZre85MlCMJJnfcGvuevv/663899QUEB1q1bh+XLlyMrKwtRUVEwmUyYP38+/ud//gcfffSRT+IwFOfFE7n++utx++23Izk5GUlJSfjv//5vJCYm+t13+vTp+POf/4y8vDzExsZi+fLluOiii3z26+zsxJEjR7zWff75537LlN18881YvXo1pk+fjujoaGRlZeGmm27CQw895LPvd999h9LS0iG/NiIiorGMSQgiIiKiAfzdNTll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qq6uDmvWrDlR+F4ClQ47US+D888/3+/6++67b9C+DJ2dnT6zNSL5vOjvZ3hXVxf++c9/DulnuN1ux7vvvus124eIiCiSMQlBREREFAaTJk3ye4Hm1Vdfxc0334xNmzahtrYWVqsVZrMZTU1N2LZtG1555RWsWrUKZ555Ju644w4cOXIkDNEHl0KhwA033OCz3uPx4Kc//SnWrVuHjo4OWCwWbNu2DT/4wQ/Q1NTks//8+fMxZcoUn/X+7ri1Wq3461//ivb2drjdbvnfybr++uuhUvlOMn711Vfxhz/8AdXV1bDb7aipqcEf//hHvxfX1Wo1Vq5cedIxhIIoivJ709XVhaqqKrz11lu47rrrcNttt/ntBaFQKPDQQw/BaDT6rA/F11mj0eDKK6/02c/lcuHmm2/G5s2b0dvbi66uLqxbtw6/+MUvhvz6zWYzbrrpJpx//vm477778O6772LPnj3o6OiAw+FAb28v9uzZg7vvvhsWi8Xn+acyq0mhUOC+++7zewd4TU0NrrzySvztb39DdXU1rFYr2tvb8dlnn+GnP/0pnnjiCb9jnnHGGbjssstOOqaRlJOT4/ccebxgzYIARvY9V6lUfmdu1dTU4K677sKRI0dgNpvxySef4Ic//CGsVuuwXou/8x4APPvss2hubobL5ZK/twcm2VauXOk3gbF//34sXboUb731Furr6+FwONDZ2Ynt27fj0UcfxSWXXIJ9+/Z5PSdSz4tAXxLC34yi1atX484778TWrVtRX18Pm82G3t5e1NXV4fPPP8dLL72Em2++GWeddRZ+85vfBOynQ0REFGlYjomIiIgoTH7zm9/gmmuu8bkI8cUXXwy79MZYd+ONN+L999/3KcXR0dGBe+6554TP1+l0AfebNm0a1q5d67P+iSee8LlwuHnzZkyYMGEYkffJzs7Gj3/8Y793+L7++ut4/fXXTzjGzTffjKysrGEfO5See+45PPfcc8N6zt13340FCxb43Raqr/NPf/pT/Pvf//ZJBDQ1NQWlt8mRI0fw1ltv4a233hrW804//fRTOu78+fNx77334o9//KPPtq6uLvzpT3/Cn/70pyGNNWHCBDz55JPDKhUTbjfccAM+//zzgNt1Oh0uvfTSoB5zJN/ziy++2G/T640bN/rtfTEc06ZN87ve3/noH//4h9yzIiUlBXfccQceeeQRn+c2NDTgvvvuG3IMkXpeBPoSVvfffz9uvvlmuFwur20bNmzAhg0bwhQZERHR6DR2fgMlIiIiijD5+fl45plnfO4YH4+MRiNefPFFpKWlDfu5Wq0Wjz/+uN9ZEEBfiRWtVnuqIZ7QHXfcMaTmtf4sWrQId9xxR3ADGmFGoxF/+tOfAvZh6N8nFF/njIwM/O53vxtSfXWtVuvTryIUli1b5re0z3DdcMMNePTRRwP2EBiKM844A//6178CNvEerc4999xBSy1dfPHFITl/jtR7vmLFCiQlJQ1pvHnz5g3r+GeeeeaQxz7eTTfdhJ/85Ccn9dzjRfJ5cd68eVi9erXfslpERETkjUkIIiIiojCaP38+1q9fP6SyIwMZDAYsWbIEubm5IYps5GVnZ2PdunVYuHDhkO/Wnjp1Kt566y1ceOGFAfdJSEjA7373u5A3NhUEAY899hjuv//+IV/sjY2Nxf/8z//gscceG7MNSnU6Ha699lps2LDBb1mk44Xq67x48WI8/PDDg144NplMePbZZzF79my/248vQ6NSqfz2ehiMUqnEDTfcgAcffHBYzxvMkiVL8M4772DhwoXD+hxnZGTg/vvvx//93/8FLM8zmgmCgOuvvz7g9lAmk0biPY+NjcUzzzyD2NjYgPsolUr85Cc/wUMPPTTkGIC+MmWrV68O2BviRH71q1/hueeeO+VZCJF+Xly0aBHefvttTJ8+fVjPi4uLw4oVKxAfHx+iyIiIiEYXlmMiIiIiCrOsrCz8/e9/R2VlJT788EPs2rULNTU16O7uhsPhgF6vR3x8PHJycjBlyhTMmzcPp5122klfXBrN4uPj8ec//xm333473n//fXz33XeoqalBV1cX3G43YmNjkZqailmzZmHBggU444wzhjTuVVddhSlTpuCNN97Azp070dzcPOwa60N1/fXXY9myZXj//fexbds2lJeXo7OzExaLBXq9HiaTCUVFRZg/fz6uuOKKYV/kHmkKhQJKpRJarRYxMTGIi4tDWloacnNzUVxcjLPOOmvYryFUX+dly5bh9NNPx6uvvoqtW7fiyJEjUKvVyMjIwIUXXojrr78eCQkJePrpp/0+32QyeS0nJibim2++QUlJCUpKSrB3717U1taiqakJZrMZbrcbUVFRMJlMyMnJwdy5c7Fw4cKgNUoeKD8/H3/+859RX1+PTz/9FNu3b0dVVRW6urrQ09MDjUaDuLg4JCcnY9asWZg3bx7OPvtsvzX5x5Jly5bhySef9Pl+zcjIGPLn4mSNxHteXFyMDRs24P/+7/+wdetWNDQ0AOgri3TmmWfi2muvxeTJk32aPg/FOeecg3fffRevv/46vvnmGzQ0NMBqtZ6w0Xq/Cy+8EBdccAG2bt2Kzz77DKWlpWhubkZPTw9UKhVMJhOSk5MxZ84cnH322ZgzZ07AsSLtvDhQYWEh1qxZg127duGjjz5CSUkJ6urq0NvbC5fLBb1ej4SEBOTm5mLq1KmYN28eiouLOYOCiIjGFUEa6m8gREREREREEeDqq69GWVmZ1zq9Xo9vvvkGGo0mTFFRIDfddBO++uorr3WrVq3C7bffHqaIiIiIiGg4WI6JiIiIiIjGvKqqKlRWVp5wv7ffftsnAQH0NZFmAmL0aWtrw/bt273WCYIwIn09iIiIiCg4xvbcXCIiIiIiIgCVlZX45S9/iXnz5uGSSy5BcXExMjIyoNPp0Nvbi3379mH9+vV47733/D7/hhtuGOGIyR9RFCGKIhwOBw4ePIhHHnkELpfLa5+zzjorJCWviIiIiCg0mIQgIiIiIqKIIEkStm3bhm3btg3reZdccsmwm8NTaPzmN7/BunXrBt3nlltuGaFoiIiIiCgYWI6JiIiIiIjGrfnz5+NPf/pTuMOgIbriiitw+umnhzsMIiIiIhoGzoQgIiIiIqIxT6lUDmv/2NhY3HLLLbjpppugUPDerLFg7ty5ePDBB8MdBhERERENE5MQREREREQ05l166aV477338Nlnn6G0tBTV1dVoaWmBzWaDUqlEdHQ0kpOTMW3aNJx++um4+OKLodVqwx02DUIQBBiNRhQUFODKK6/E1VdfPexkExERERGFnyBJkhTuIIiIiIiIiIiIiIiIKPJw3jEREREREREREREREYUEkxBERERERERERERERBQSTEIQEREREREREREREVFIMAlBREREREREREREREQhoQp3AKGwb98+/L//9/+wfft2NDU1we12IykpCcXFxVi6dCnOPvvsIY/12WefYe3atSgtLUVbWxuMRiMmTJiASy+9FNdccw30ev2Qx9q1axfeeustbN++Ha2trdBqtcjMzMSCBQtw7bXXwmQynczLJSIiIiIiIiIiIiIalQRJkqRwBxEsbrcb//u//4tXXnll0P0WLlyIRx55BFqtNuA+TqcT99xzDz744IOA+2RnZ+Ppp5/GlClTBj2eJEl45JFH8MorryDQ252YmIjHHnsM8+fPH3QsIiIiIiIiIiIiIqKxIqKSEL/97W+xZs0aAIBarcaiRYswd+5caLVaHDx4EGvWrEFzczMAYMGCBXjmmWcgCILfse68805s2LABABAXF4fly5ejoKAAnZ2deO+991BWVgYASEpKwttvv420tLSAcT322GN46aWXAAB6vR5XXXUVZsyYAavVis2bN+PLL7+Ut/3zn/9EYWFhcN4QIiIiIiIiIiIiIqIwipgkxNatW/HTn/4UAGAwGPDyyy9jxowZXvuYzWbccsst+O677wAAjz76KJYsWeIz1pYtW/Dzn/8cAJCeno433ngD6enp8nZRFPHb3/4Wa9euBQBccskleOqpp/zGtXfvXixbtgySJCE6Ohqvv/66z8yJp59+Gs888wwAYPr06Xj77bcDJkeIiIiIiIiIiIiIiMaKiGlM/dprr8mP77rrLp8EBAAYjUY8/vjjUKvVAIAnn3zSb3mk/oQAADzwwANeCQgAUCgU+N3vfiev37RpEyorK/3G9eyzz8rHuPPOO/2Wbrr11lvleHfv3o2tW7cO+lqJiIiIiIiIiIiIiMaCiEhCiKKI7du3AwAEQcCiRYsC7puamoozzjgDANDY2IgdO3Z4ba+pqUFFRQUAICcnB+edd57fcaKionD11VfLyx9++KHPPmazGZ999hmAvgTIsmXL/I4lCAJWrlwpL/eXgSIiIiIiIiIiIiIiGssiIgnR1dUFu90OAEhISEBsbOyg++fk5MiPj5918MUXX8iPzz777EHHOeecc+THn3/+uc/27du3w+l0AgDmzp0LnU530mMREREREREREREREY01qnAHEAyn0tbi+DJKA5enTp066HMLCwuhVCrh8Xhw8OBBSJLk1cuhqqpqyGOZTCZkZGSgoaEBHR0daG9vR0JCwqDPOX4WBxERERERERERERFRqMyZM2fYz4mImRCxsbFyn4eOjg709PQMun9NTY38+NChQwG3ZWRkDDqOSqVCSkoKAMBqtaK5udlr+8CxTzQWAK/eE8fHRUREREREREREREQ01kTETAiVSoUZM2Zgx44dEEUR//73v3H99df73be5uRnbtm2Tl49PWPT29sqP4+PjT3jsuLg4NDY2ymOlpqae0lj+nnsier1+yPtGIpvNBgCDlrsiIgonnqeIaLTjeYqIRjuep4hotON5iiKd1Wo96edGxEwIALjmmmvkx0888QTKy8t99rFYLPjVr34Fl8slrzObzV77DHwztVrtCY87cB+LxRKysYiIiIiIiIiIiIiIxpqImAkBAIsWLcK6deuwbds2mM1mXHvttbjyyisxd+5caLVaHDx4EO+88w6ampqQlZWFuro6AIBCMfbzMIWFheEOIawqKioA8H0gotGL5ykiGu14niKi0Y7nKSIa7Xieokh3Kv2JIyYJoVQq8fTTT+OXv/wlPvvsM7hcLrzzzjt45513vPabNm0afvWrX+HGG28EAMTExHhtH1jayOFwnPC4A/cxGAwhG4uIiIiIiIiIiIiIaKyJmCQE0JdQeOmll/Cf//wH69atQ2lpKTo6OhAVFYX8/HwsWrQIy5cvx3fffSc/JykpyWuM6Oho+XFnZ+cJj9nV1eV1/GCNNfC5RERERERERERERERjUUQlIfpdcMEFuOCCCwJuP3jwoPx4+vTpXttycnLwzTffAAAaGhoGPY7b7UZzczOAvlkPKSkpXttzc3PlxycaC4Dc4Pr45xIRERERERERERERjUVjvyHCSfj222/lx3PmzPHaVlBQID/es2fPoONUVFTA4/EAAPLz8yEIgtf2SZMmDXmsjo4OOVFhMpmQkJAw6P5ERERERERERERERKPduEtCdHR04NNPPwXQVz7p4osv9tp+9tlny4+/+OKLQcf6/PPP5cfnnHOOz/bTTz8dGo0GALB9+3bY7faTHouIiIiIiIiIiIiIaKwZd0mIRx99VE4GXHfdddDpdF7bc3JyUFRUBACoqanB1q1b/Y7jcDjw9ttvy8uXXXaZzz4GgwHnnXceAMBsNmPt2rV+x5IkCW+88Ya8vHDhwmG8IiIiIiIiIiIiIiKi0SmikhAlJSVwOp1+tzmdTqxevRrr168HAOTl5WHVqlV+9/35z38uP/7973/v1asBAERR9Fp/ySWXeJVxGmjVqlVymaYnnngC+/bt89nn2WefRWlpKYC+HhXnn39+4BdJRERERERERERERDRGRFRj6ueffx67du3CueeeixkzZiApKQl2ux0HDhzAhx9+KPdcSElJwfPPPw+tVut3nAULFmDhwoXYsGEDGhoasHTpUlx77bUo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\n",
      "text/plain": [
       "<Figure size 792x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "image/png": {
       "height": 280,
       "width": 784
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "### Using the same layout as seen in the first lesson of the Kaggle Time Series Course\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "plt.style.use(\"seaborn-whitegrid\")\n",
    "plt.rc(\n",
    "    \"figure\",\n",
    "    autolayout=True,\n",
    "    figsize=(11, 4),\n",
    "    titlesize=18,\n",
    "    titleweight='bold',\n",
    ")\n",
    "plt.rc(\n",
    "    \"axes\",\n",
    "    labelweight=\"bold\",\n",
    "    labelsize=\"large\",\n",
    "    titleweight=\"bold\",\n",
    "    titlesize=16,\n",
    "    titlepad=10,\n",
    ")\n",
    "%config InlineBackend.figure_format = 'retina'\n",
    "\n",
    "fig, ax = plt.subplots()\n",
    "ax.plot(\"Time Step\", \"Animal_Type\", data=monthly, color='0.75')\n",
    "ax = sns.regplot(x='Time Step', y='Animal_Type', data=monthly, ci=None)\n",
    "ax.set_title('TIme Plot of Dogs Only Outcome')\n",
    "                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "288ad6fd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:54.004716Z",
     "iopub.status.busy": "2024-10-11T19:10:54.003657Z",
     "iopub.status.idle": "2024-10-11T19:10:54.008225Z",
     "shell.execute_reply": "2024-10-11T19:10:54.008818Z",
     "shell.execute_reply.started": "2022-12-16T15:24:42.84959Z"
    },
    "papermill": {
     "duration": 0.109408,
     "end_time": "2024-10-11T19:10:54.009016",
     "exception": false,
     "start_time": "2024-10-11T19:10:53.899608",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Lag_1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-03-31</th>\n",
       "      <td>828</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-04-30</th>\n",
       "      <td>359</td>\n",
       "      <td>828.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-05-31</th>\n",
       "      <td>379</td>\n",
       "      <td>359.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-06-30</th>\n",
       "      <td>490</td>\n",
       "      <td>379.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-07-31</th>\n",
       "      <td>458</td>\n",
       "      <td>490.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Animal_Type  Lag_1\n",
       "Outcome Date                    \n",
       "2020-03-31            828    NaN\n",
       "2020-04-30            359  828.0\n",
       "2020-05-31            379  359.0\n",
       "2020-06-30            490  379.0\n",
       "2020-07-31            458  490.0"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Add lag feature to shift the observations of the target series\n",
    "\n",
    "monthly['Lag_1'] = monthly['Animal_Type'].shift(1)\n",
    "\n",
    "df = monthly.reindex(columns=['Animal_Type', 'Lag_1'])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "30b610bb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:54.225257Z",
     "iopub.status.busy": "2024-10-11T19:10:54.206636Z",
     "iopub.status.idle": "2024-10-11T19:10:54.538266Z",
     "shell.execute_reply": "2024-10-11T19:10:54.539150Z",
     "shell.execute_reply.started": "2022-12-16T15:24:44.536969Z"
    },
    "papermill": {
     "duration": 0.441675,
     "end_time": "2024-10-11T19:10:54.539394",
     "exception": false,
     "start_time": "2024-10-11T19:10:54.097719",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 792x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "image/png": {
       "height": 280,
       "width": 285
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "### Lag Plot of Dog Outcomes\n",
    "fig, ax = plt.subplots()\n",
    "ax = sns.regplot(x='Lag_1', y='Animal_Type', data=monthly, ci=None)\n",
    "ax.set_aspect('equal')\n",
    "ax.set_title('Lag Plot of Dog Outcomes');"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb0ca8be",
   "metadata": {
    "papermill": {
     "duration": 0.089829,
     "end_time": "2024-10-11T19:10:54.721414",
     "exception": false,
     "start_time": "2024-10-11T19:10:54.631585",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Asking a New Question"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "317a5de2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:54.914734Z",
     "iopub.status.busy": "2024-10-11T19:10:54.911215Z",
     "iopub.status.idle": "2024-10-11T19:10:54.961092Z",
     "shell.execute_reply": "2024-10-11T19:10:54.961728Z",
     "shell.execute_reply.started": "2022-12-16T15:24:48.684371Z"
    },
    "papermill": {
     "duration": 0.148377,
     "end_time": "2024-10-11T19:10:54.961928",
     "exception": false,
     "start_time": "2024-10-11T19:10:54.813551",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Found Location</th>\n",
       "      <th>Intake Type</th>\n",
       "      <th>Intake Condition</th>\n",
       "      <th>Sex upon Intake</th>\n",
       "      <th>Age upon Intake</th>\n",
       "      <th>Breed</th>\n",
       "      <th>Date of Birth</th>\n",
       "      <th>Outcome Type</th>\n",
       "      <th>Outcome Subtype</th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Sex upon Outcome</th>\n",
       "      <th>Age upon Outcome</th>\n",
       "      <th>Color</th>\n",
       "      <th>Intake Date</th>\n",
       "      <th>Intake Month</th>\n",
       "      <th>Stay_Duration</th>\n",
       "      <th>Year</th>\n",
       "      <th>Month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>A836850</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>6111 Softwood Drive in Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Pregnant</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>06/15/2017</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Blue/White</td>\n",
       "      <td>2021-06-15</td>\n",
       "      <td>June 2021</td>\n",
       "      <td>1 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>A815227</td>\n",
       "      <td>Baby</td>\n",
       "      <td>12305 Zeller Lane in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Norfolk Terrier</td>\n",
       "      <td>01/12/2020</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Brown/Cream</td>\n",
       "      <td>2020-03-12</td>\n",
       "      <td>March 2020</td>\n",
       "      <td>1 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>Thaxton And Sassman in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>1 year</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2019-01-07</td>\n",
       "      <td>January 2019</td>\n",
       "      <td>636 days</td>\n",
       "      <td>2019</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>1709 Colony Creek Drive in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>5 months</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2018-05-23</td>\n",
       "      <td>May 2018</td>\n",
       "      <td>865 days</td>\n",
       "      <td>2018</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>126</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>2604 Aldrich in Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2020-09-22</td>\n",
       "      <td>September 2020</td>\n",
       "      <td>12 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175018</th>\n",
       "      <td>A849492</td>\n",
       "      <td>*Dill</td>\n",
       "      <td>7011 Millrace Drive in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Chihuahua Shorthair</td>\n",
       "      <td>01/10/2020</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2022-01-10</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>4 days</td>\n",
       "      <td>2022</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175023</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Owner Surrender</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2022-01-10</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>-18 days</td>\n",
       "      <td>2022</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175024</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>12041 Harris Branch Parkway in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>2 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2021-12-13</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>10 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175025</th>\n",
       "      <td>A848504</td>\n",
       "      <td>Eros</td>\n",
       "      <td>124 W Anderson Ln in Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>12/21/2019</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown/Brown</td>\n",
       "      <td>2021-12-21</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>26 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175033</th>\n",
       "      <td>A848107</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>14402 Callan in Travis (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Shih Tzu</td>\n",
       "      <td>12/14/2010</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2021-12-14</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>6 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>14150 rows × 20 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Animal ID   Name                              Found Location  \\\n",
       "28       A836850   <NA>          6111 Softwood Drive in Austin (TX)   \n",
       "38       A815227   Baby            12305 Zeller Lane in Austin (TX)   \n",
       "120      A772747  Lamar          Thaxton And Sassman in Austin (TX)   \n",
       "123      A772747  Lamar      1709 Colony Creek Drive in Austin (TX)   \n",
       "126      A772747  Lamar                 2604 Aldrich in Austin (TX)   \n",
       "...          ...    ...                                         ...   \n",
       "175018   A849492  *Dill          7011 Millrace Drive in Austin (TX)   \n",
       "175023   A848016  Honey                                 Austin (TX)   \n",
       "175024   A848016  Honey  12041 Harris Branch Parkway in Austin (TX)   \n",
       "175025   A848504   Eros            124 W Anderson Ln in Austin (TX)   \n",
       "175033   A848107   <NA>                 14402 Callan in Travis (TX)   \n",
       "\n",
       "            Intake Type Intake Condition Sex upon Intake Age upon Intake  \\\n",
       "28        Public Assist         Pregnant   Intact Female         4 years   \n",
       "38                Stray           Normal   Intact Female         1 month   \n",
       "120               Stray           Normal   Neutered Male          1 year   \n",
       "123               Stray           Normal     Intact Male        5 months   \n",
       "126       Public Assist           Normal   Neutered Male         2 years   \n",
       "...                 ...              ...             ...             ...   \n",
       "175018            Stray           Normal     Intact Male         2 years   \n",
       "175023  Owner Surrender           Normal   Spayed Female        3 months   \n",
       "175024            Stray           Normal   Intact Female        2 months   \n",
       "175025            Stray           Normal     Intact Male         2 years   \n",
       "175033            Stray           Normal   Spayed Female        11 years   \n",
       "\n",
       "                                 Breed Date of Birth     Outcome Type  \\\n",
       "28                            Pit Bull    06/15/2017         Transfer   \n",
       "38                     Norfolk Terrier    01/12/2020  Return to Owner   \n",
       "120     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "123     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "126     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "...                                ...           ...              ...   \n",
       "175018             Chihuahua Shorthair    01/10/2020         Transfer   \n",
       "175023             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175024             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175025                        Pit Bull    12/21/2019         Adoption   \n",
       "175033                        Shih Tzu    12/14/2010         Transfer   \n",
       "\n",
       "       Outcome Subtype Animal_Type Sex upon Outcome Age upon Outcome  \\\n",
       "28             Partner         Dog    Intact Female          4 years   \n",
       "38                 NaN         Dog    Intact Female          1 month   \n",
       "120                NaN         Dog    Neutered Male          2 years   \n",
       "123                NaN         Dog    Neutered Male          2 years   \n",
       "126                NaN         Dog    Neutered Male          2 years   \n",
       "...                ...         ...              ...              ...   \n",
       "175018         Partner         Dog      Intact Male          2 years   \n",
       "175023             NaN         Dog    Spayed Female         3 months   \n",
       "175024             NaN         Dog    Spayed Female         3 months   \n",
       "175025             NaN         Dog    Neutered Male          2 years   \n",
       "175033         Partner         Dog    Spayed Female         11 years   \n",
       "\n",
       "              Color Intake Date    Intake Month Stay_Duration  Year  Month  \n",
       "28       Blue/White  2021-06-15       June 2021        1 days  2021      6  \n",
       "38      Brown/Cream  2020-03-12      March 2020        1 days  2020      3  \n",
       "120           White  2019-01-07    January 2019      636 days  2019      1  \n",
       "123           White  2018-05-23        May 2018      865 days  2018      5  \n",
       "126           White  2020-09-22  September 2020       12 days  2020      9  \n",
       "...             ...         ...             ...           ...   ...    ...  \n",
       "175018        Brown  2022-01-10    January 2022        4 days  2022      1  \n",
       "175023     Tricolor  2022-01-10    January 2022      -18 days  2022      1  \n",
       "175024     Tricolor  2021-12-13   December 2021       10 days  2021     12  \n",
       "175025  Brown/Brown  2021-12-21   December 2021       26 days  2021     12  \n",
       "175033        Brown  2021-12-14   December 2021        6 days  2021     12  \n",
       "\n",
       "[14150 rows x 20 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Asking a New Question\n",
    "\n",
    "Dog_Intake = Dog.drop(columns=['Outcome Date', 'Outcome Month'])\n",
    "Dog_Intake['Year'] = pd.DatetimeIndex(Dog_Intake['Intake Date']).year\n",
    "Dog_Intake['Month'] = pd.DatetimeIndex(Dog_Intake['Intake Date']).month\n",
    "Dog_Intake"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c18bd087",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:55.158726Z",
     "iopub.status.busy": "2024-10-11T19:10:55.157500Z",
     "iopub.status.idle": "2024-10-11T19:10:55.673825Z",
     "shell.execute_reply": "2024-10-11T19:10:55.674491Z",
     "shell.execute_reply.started": "2022-12-16T15:25:02.374354Z"
    },
    "papermill": {
     "duration": 0.620712,
     "end_time": "2024-10-11T19:10:55.674708",
     "exception": false,
     "start_time": "2024-10-11T19:10:55.053996",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Animal ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Found Location</th>\n",
       "      <th>Intake Type</th>\n",
       "      <th>Intake Condition</th>\n",
       "      <th>Sex upon Intake</th>\n",
       "      <th>Age upon Intake</th>\n",
       "      <th>Breed</th>\n",
       "      <th>Date of Birth</th>\n",
       "      <th>Outcome Type</th>\n",
       "      <th>Outcome Subtype</th>\n",
       "      <th>Animal_Type</th>\n",
       "      <th>Sex upon Outcome</th>\n",
       "      <th>Age upon Outcome</th>\n",
       "      <th>Color</th>\n",
       "      <th>Outcome Date</th>\n",
       "      <th>Outcome Month</th>\n",
       "      <th>Stay_Duration</th>\n",
       "      <th>Year</th>\n",
       "      <th>Month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>A836850</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>6111 Softwood Drive Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Pregnant</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>06/15/2017</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>4 years</td>\n",
       "      <td>Blue/White</td>\n",
       "      <td>2021-06-16</td>\n",
       "      <td>June 2021</td>\n",
       "      <td>1 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>A815227</td>\n",
       "      <td>Baby</td>\n",
       "      <td>12305 Zeller Lane Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Norfolk Terrier</td>\n",
       "      <td>01/12/2020</td>\n",
       "      <td>Return to Owner</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>1 month</td>\n",
       "      <td>Brown/Cream</td>\n",
       "      <td>2020-03-13</td>\n",
       "      <td>March 2020</td>\n",
       "      <td>1 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>Thaxton And Sassman Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>1 year</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>636 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>1709 Colony Creek Drive Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>5 months</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>865 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>126</th>\n",
       "      <td>A772747</td>\n",
       "      <td>Lamar</td>\n",
       "      <td>2604 Aldrich Austin (TX)</td>\n",
       "      <td>Public Assist</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull/Australian Cattle Dog</td>\n",
       "      <td>11/23/2017</td>\n",
       "      <td>Rto-Adopt</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>White</td>\n",
       "      <td>2020-10-04</td>\n",
       "      <td>October 2020</td>\n",
       "      <td>12 days</td>\n",
       "      <td>2020</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175018</th>\n",
       "      <td>A849492</td>\n",
       "      <td>*Dill</td>\n",
       "      <td>7011 Millrace Drive Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Chihuahua Shorthair</td>\n",
       "      <td>01/10/2020</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2022-01-14</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>4 days</td>\n",
       "      <td>2022</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175023</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>Austin (TX)</td>\n",
       "      <td>Owner Surrender</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2021-12-23</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>-18 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175024</th>\n",
       "      <td>A848016</td>\n",
       "      <td>Honey</td>\n",
       "      <td>12041 Harris Branch Parkway Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Female</td>\n",
       "      <td>2 months</td>\n",
       "      <td>German Shepherd Mix</td>\n",
       "      <td>09/13/2021</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>3 months</td>\n",
       "      <td>Tricolor</td>\n",
       "      <td>2021-12-23</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>10 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175025</th>\n",
       "      <td>A848504</td>\n",
       "      <td>Eros</td>\n",
       "      <td>124 W Anderson Ln Austin (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Intact Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Pit Bull</td>\n",
       "      <td>12/21/2019</td>\n",
       "      <td>Adoption</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Neutered Male</td>\n",
       "      <td>2 years</td>\n",
       "      <td>Brown/Brown</td>\n",
       "      <td>2022-01-16</td>\n",
       "      <td>January 2022</td>\n",
       "      <td>26 days</td>\n",
       "      <td>2022</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175033</th>\n",
       "      <td>A848107</td>\n",
       "      <td>&lt;NA&gt;</td>\n",
       "      <td>14402 Callan Travis (TX)</td>\n",
       "      <td>Stray</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Shih Tzu</td>\n",
       "      <td>12/14/2010</td>\n",
       "      <td>Transfer</td>\n",
       "      <td>Partner</td>\n",
       "      <td>Dog</td>\n",
       "      <td>Spayed Female</td>\n",
       "      <td>11 years</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2021-12-20</td>\n",
       "      <td>December 2021</td>\n",
       "      <td>6 days</td>\n",
       "      <td>2021</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>14150 rows × 20 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Animal ID   Name                           Found Location  \\\n",
       "28       A836850   <NA>          6111 Softwood Drive Austin (TX)   \n",
       "38       A815227   Baby            12305 Zeller Lane Austin (TX)   \n",
       "120      A772747  Lamar          Thaxton And Sassman Austin (TX)   \n",
       "123      A772747  Lamar      1709 Colony Creek Drive Austin (TX)   \n",
       "126      A772747  Lamar                 2604 Aldrich Austin (TX)   \n",
       "...          ...    ...                                      ...   \n",
       "175018   A849492  *Dill          7011 Millrace Drive Austin (TX)   \n",
       "175023   A848016  Honey                              Austin (TX)   \n",
       "175024   A848016  Honey  12041 Harris Branch Parkway Austin (TX)   \n",
       "175025   A848504   Eros            124 W Anderson Ln Austin (TX)   \n",
       "175033   A848107   <NA>                 14402 Callan Travis (TX)   \n",
       "\n",
       "            Intake Type Intake Condition Sex upon Intake Age upon Intake  \\\n",
       "28        Public Assist         Pregnant   Intact Female         4 years   \n",
       "38                Stray           Normal   Intact Female         1 month   \n",
       "120               Stray           Normal   Neutered Male          1 year   \n",
       "123               Stray           Normal     Intact Male        5 months   \n",
       "126       Public Assist           Normal   Neutered Male         2 years   \n",
       "...                 ...              ...             ...             ...   \n",
       "175018            Stray           Normal     Intact Male         2 years   \n",
       "175023  Owner Surrender           Normal   Spayed Female        3 months   \n",
       "175024            Stray           Normal   Intact Female        2 months   \n",
       "175025            Stray           Normal     Intact Male         2 years   \n",
       "175033            Stray           Normal   Spayed Female        11 years   \n",
       "\n",
       "                                 Breed Date of Birth     Outcome Type  \\\n",
       "28                            Pit Bull    06/15/2017         Transfer   \n",
       "38                     Norfolk Terrier    01/12/2020  Return to Owner   \n",
       "120     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "123     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "126     Pit Bull/Australian Cattle Dog    11/23/2017        Rto-Adopt   \n",
       "...                                ...           ...              ...   \n",
       "175018             Chihuahua Shorthair    01/10/2020         Transfer   \n",
       "175023             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175024             German Shepherd Mix    09/13/2021         Adoption   \n",
       "175025                        Pit Bull    12/21/2019         Adoption   \n",
       "175033                        Shih Tzu    12/14/2010         Transfer   \n",
       "\n",
       "       Outcome Subtype Animal_Type Sex upon Outcome Age upon Outcome  \\\n",
       "28             Partner         Dog    Intact Female          4 years   \n",
       "38                 NaN         Dog    Intact Female          1 month   \n",
       "120                NaN         Dog    Neutered Male          2 years   \n",
       "123                NaN         Dog    Neutered Male          2 years   \n",
       "126                NaN         Dog    Neutered Male          2 years   \n",
       "...                ...         ...              ...              ...   \n",
       "175018         Partner         Dog      Intact Male          2 years   \n",
       "175023             NaN         Dog    Spayed Female         3 months   \n",
       "175024             NaN         Dog    Spayed Female         3 months   \n",
       "175025             NaN         Dog    Neutered Male          2 years   \n",
       "175033         Partner         Dog    Spayed Female         11 years   \n",
       "\n",
       "              Color Outcome Date  Outcome Month Stay_Duration  Year  Month  \n",
       "28       Blue/White   2021-06-16      June 2021        1 days  2021      6  \n",
       "38      Brown/Cream   2020-03-13     March 2020        1 days  2020      3  \n",
       "120           White   2020-10-04   October 2020      636 days  2020     10  \n",
       "123           White   2020-10-04   October 2020      865 days  2020     10  \n",
       "126           White   2020-10-04   October 2020       12 days  2020     10  \n",
       "...             ...          ...            ...           ...   ...    ...  \n",
       "175018        Brown   2022-01-14   January 2022        4 days  2022      1  \n",
       "175023     Tricolor   2021-12-23  December 2021      -18 days  2021     12  \n",
       "175024     Tricolor   2021-12-23  December 2021       10 days  2021     12  \n",
       "175025  Brown/Brown   2022-01-16   January 2022       26 days  2022      1  \n",
       "175033        Brown   2021-12-20  December 2021        6 days  2021     12  \n",
       "\n",
       "[14150 rows x 20 columns]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Dog_Outcome = Dog.drop(columns=['Intake Date', 'Intake Month'])\n",
    "Dog_Outcome['Year'] = pd.DatetimeIndex(Dog_Outcome['Outcome Date']).year\n",
    "Dog_Outcome['Month'] = pd.DatetimeIndex(Dog_Outcome['Outcome Date']).month\n",
    "Dog_Outcome\n",
    "\n",
    "## FiX 'Found Location' so it works better with mapping\n",
    "Dog_Outcome = Dog_Outcome.replace(to_replace = ' in ', value=' ', regex=True)\n",
    "Dog_Outcome"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9cc2b6bc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:55.873676Z",
     "iopub.status.busy": "2024-10-11T19:10:55.872547Z",
     "iopub.status.idle": "2024-10-11T19:10:55.892687Z",
     "shell.execute_reply": "2024-10-11T19:10:55.892009Z",
     "shell.execute_reply.started": "2022-12-16T15:25:03.696627Z"
    },
    "papermill": {
     "duration": 0.125194,
     "end_time": "2024-10-11T19:10:55.892865",
     "exception": false,
     "start_time": "2024-10-11T19:10:55.767671",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Animal ID</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Intake Type</th>\n",
       "      <th>Outcome Type</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"7\" valign=\"top\">Abandoned</th>\n",
       "      <th>Adoption</th>\n",
       "      <td>163</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Died</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Disposal</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euthanasia</th>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return to Owner</th>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rto-Adopt</th>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Transfer</th>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euthanasia Request</th>\n",
       "      <th>Euthanasia</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Owner Surrender</th>\n",
       "      <th>Adoption</th>\n",
       "      <td>3437</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Died</th>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Disposal</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euthanasia</th>\n",
       "      <td>55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Missing</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return to Owner</th>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rto-Adopt</th>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Transfer</th>\n",
       "      <td>763</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Public Assist</th>\n",
       "      <th>Adoption</th>\n",
       "      <td>259</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Died</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Disposal</th>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euthanasia</th>\n",
       "      <td>59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Missing</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return to Owner</th>\n",
       "      <td>852</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rto-Adopt</th>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Transfer</th>\n",
       "      <td>106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"8\" valign=\"top\">Stray</th>\n",
       "      <th>Adoption</th>\n",
       "      <td>4158</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Died</th>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Disposal</th>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euthanasia</th>\n",
       "      <td>87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Missing</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return to Owner</th>\n",
       "      <td>1780</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rto-Adopt</th>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Transfer</th>\n",
       "      <td>1668</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wildlife</th>\n",
       "      <th>Return to Owner</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Animal ID\n",
       "Intake Type        Outcome Type              \n",
       "Abandoned          Adoption               163\n",
       "                   Died                     2\n",
       "                   Disposal                 4\n",
       "                   Euthanasia               5\n",
       "                   Return to Owner         43\n",
       "                   Rto-Adopt                7\n",
       "                   Transfer                81\n",
       "Euthanasia Request Euthanasia               1\n",
       "Owner Surrender    Adoption              3437\n",
       "                   Died                    27\n",
       "                   Disposal                 4\n",
       "                   Euthanasia              55\n",
       "                   Missing                  1\n",
       "                   Return to Owner        200\n",
       "                   Rto-Adopt               80\n",
       "                   Transfer               763\n",
       "Public Assist      Adoption               259\n",
       "                   Died                     1\n",
       "                   Disposal                 3\n",
       "                   Euthanasia              59\n",
       "                   Missing                  1\n",
       "                   Return to Owner        852\n",
       "                   Rto-Adopt               43\n",
       "                   Transfer               106\n",
       "Stray              Adoption              4158\n",
       "                   Died                    34\n",
       "                   Disposal                16\n",
       "                   Euthanasia              87\n",
       "                   Missing                  2\n",
       "                   Return to Owner       1780\n",
       "                   Rto-Adopt              182\n",
       "                   Transfer              1668\n",
       "Wildlife           Return to Owner          1"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "### What does Intake to Outcome look like?\n",
    "in_to_out = Dog_Outcome[['Animal ID', 'Intake Type', 'Outcome Type']].groupby(['Intake Type', 'Outcome Type']).count()\n",
    "in_to_out"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5d1ea3f7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:56.097595Z",
     "iopub.status.busy": "2024-10-11T19:10:56.096337Z",
     "iopub.status.idle": "2024-10-11T19:10:57.373389Z",
     "shell.execute_reply": "2024-10-11T19:10:57.374281Z",
     "shell.execute_reply.started": "2022-12-16T15:25:07.502577Z"
    },
    "papermill": {
     "duration": 1.388472,
     "end_time": "2024-10-11T19:10:57.374552",
     "exception": false,
     "start_time": "2024-10-11T19:10:55.986080",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Intake Type', ylabel='Count'>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAACzEAAAhhCAYAAABv3IDIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAABYlAAAWJQFJUiTwAAEAAElEQVR4nOzcebzXc94//kenU7QnJSq7cTpJVEqM7YoRCVO2LNmX4VszdhnXDBeXwYxl5iqTyJplFGUp4iqGslRzZGxZxhJKSdoIbef3h1/ncuacEnJOuN9vt3Obc16v5+v1er7fyufWePSqUVpaWhoAAAAAAAAAAAAAgCpSUN0NAAAAAAAAAAAAAAA/LULMAAAAAAAAAAAAAECVEmIGAAAAAAAAAAAAAKqUEDMAAAAAAAAAAAAAUKWEmAEAAAAAAAAAAACAKiXEDAAAAAAAAAAAAABUKSFmAAAAAAAAAAAAAKBKCTEDAAAAAAAAAAAAAFVKiBkAAAAAAAAAAAAAqFJCzAAAAAAAAAAAAABAlRJiBgAAAAAAAAAAAACqlBAzAAAAAAAAAAAAAFClCqu7AapfSUlJdbcAAAAAAAAAAAAAwA9Ux44dv/EaNzEDAAAAAAAAAAAAAFXKTcyU+TYpeICfgqlTpyZJiouLq7kTAH7MfN4AUBV83gBQVXzmAFAVfN4AUBV83gCsWklJybde6yZmAAAAAAAAAAAAAKBKCTEDAAAAAAAAAAAAAFVKiBkAAAAAAAAAAAAAqFJCzAAAAAAAAAAAAABAlRJiBgAAAAAAAAAAAACqlBAzAAAAAAAAAAAAAFClhJgBAAAAAAAAAAAAgColxAwAAAAAAAAAAAAAVCkhZgAAAAAAAAAAAACgSgkxAwAAAAAAAAAAAABVSogZAAAAAAAAAAAAAKhSQswAAAAAAAAAAAAAQJUSYgYAAAAAAAAAAAAAqpQQMwAAAAAAAAAAAABQpYSYAQAAAAAAAAAAAIAqJcQMAAAAAAAAAAAAAFQpIWYAAAAAAAAAAAAAoEoVVncDAAAAAAAAAAAAAD8UL774Yu68885MmjQps2fPTmFhYVq2bJlddtklxx57bJo3b75Gzunfv39GjhyZcePGpVWrVmtkzx+yoqKib1R/2WWXpVevXt9TN6wJQswAAAAAAAAAAAAAX6O0tDRXXnllhgwZksLCwuy8887ZZ599smTJkkyZMiU33XRT7rrrrlx++eXZZ599qrvdH52+fftWGLv11luzcOHCHH300WnYsGG5ueLi4qpqjW9JiBkAAAAAAAAAAADga1x77bUZMmRIWrZsmcGDB+dnP/tZuflHHnkk55xzTs4888w0btw4Xbp0qaZOf5z69etXYWzkyJFZuHBhjjnmGLdV/wAVVHcDAAAAAAAAAAAAAGuz999/P4MGDUqtWrUyaNCgCgHmJOnWrVvOP//8LFu2LBdddFGWL19eNjdgwIAUFRVl4sSJle5dVFSU/v37l40VFRVl5MiRSZI999wzRUVFKSoqSteuXcutnTdvXq655pr06NEj2223XTp27JgDDjggV155ZRYtWlSu9p133sm5556bXXfdNW3bts0uu+ySc889N++8806Fnr7a76hRo9KrV69st9122WWXXXLZZZdl8eLFSZJnnnkmffr0SYcOHdKpU6ecc845mTt3bqXvcObMmbn44ouz5557pm3bttlxxx3zq1/9Ki+88MJK3vo3t2zZsuy+++7p0KFDPv3000prLrnkkhQVFWXMmDFlY0VFRenTp09mzZqVc845JzvttFPatWuXXr165cEHH1zpeePHj89JJ52UHXfcMW3bts1ee+2VK664IgsWLFhjz/Rj5iZmAAAAAAAAAAAAgFUYMWJEli5dmn333TdFRUUrrTvkkENy7bXX5u23386kSZO+9W3Mffv2zdixY/Pqq6/m6KOPTsOGDZMkDRo0KKt57733cswxx2T69OnZZpttcvjhh2f58uV55513csstt6R3796pW7dukuSFF17Icccdl08//TRdu3bNVlttlbfeeisPPPBAxo0bl5tvvjnt2rWr0Mftt9+eJ598MnvttVc6d+6cp556Krfcckvmz5+fPffcM2eccUb22GOPHHbYYZkyZUoeeOCBzJ07N0OGDCm3z8svv5zjjz8+8+fPzy677JK99947c+fOzdixY3PEEUfk2muvze677/6t3tVX1axZM4ccckgGDBiQ0aNH59BDDy03//nnn+eBBx5Is2bNsueee5abmz9/fg4//PA0aNAgvXr1ysKFC/Pwww/n7LPPzqxZs3LiiSeWqx84cGAGDBiQxo0bZ4899kiTJk3y+uuv56abbsqTTz6Zu+++O/Xr1//Oz/RjJsQMAAAAAAAAAAAAsAolJSVJkp133nmVdYWFhdlxxx0zatSoPPfcc986xNyvX79Mnz49r776ao455pi0atWqQs0555yT6dOn58wzz8wpp5xSbu7jjz9OvXr1kiSlpaU577zz8sknn+RPf/pTDjjggLK6hx56KGeccUbOPffcPPTQQykoKCi3z9NPP50RI0Zkyy23TJIsXrw4PXv2zP3335/HH388N910Uzp37pwkWb58eU444YSMHz8+U6dOTXFxcZJk6dKlOf3007No0aLcdtttZfVJMmvWrBx88MG54IIL8thjj6V27drf6n191aGHHppBgwblb3/7W4UQ80MPPZQFCxbkV7/6VWrVqlVu7rXXXss+++yTa665puw9nHTSSTnooIPy5z//Od26dcvGG2+cJHn22WczYMCAtG/fPtdff31ZyDz5MvB+/vnn53/+53/y29/+9js/z49ZwdeXAAAAAAAAAAAAAPx0zZ49O0my4YYbfm3tRhttlCT58MMPv7d+XnrppUyZMiXFxcU56aSTKsw3adIk66yzTpLkueeey1tvvZX27duXCzAnSffu3dOxY8e8/fbbZUHtr+rTp09ZgDlJateunX333TfLly/P7rvvXi6QXFBQULb/q6++Wjb+97//Pe+++26OOuqocvVJ0rx585x44omZPXt2nnnmmW/xJiraYIMNsueee+bll1/OSy+9VG7u7rvvTkFBQQ455JAK62rWrJmzzz67XJB74403Tp8+fbJkyZLcf//9ZeNDhw5NklxyySXlAsxJ0qtXrxQXF+fBBx9cI8/zY+YmZgAAAAAAAAAAAIAfkH/+859Jkl122aXC7cn/7pVXXkmS7LjjjpXOd+nSJSUlJXnllVfSqVOncnNt27atUN+8efMkyTbbbLPSuZkzZ5aNPf/880mSGTNmZMCAARXWvPPOO0mSN998M7vvvvsqn2V1HXHEEXnkkUdy9913lz3Da6+9lueffz677bZbpTdbb7TRRmU3LX/ViuD1iveYfPlMtWrVypgxYzJmzJgKa5YsWZKPP/44c+fOzXrrrbdGnunHSIgZAAAAAAAAAAAAYBWaNm2aN998s1w4d2U++OCDJF/eCPx9WbBgQZL/Cw2vysKFC1fZT7NmzcrVfVWDBg0qjNWsWfNr55YuXVo2Nm/evCSpNOz7VYsWLVrl/DfRpUuXbLnllhk1alTOO++81K9fP8OGDUuSHHbYYZWuadq0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off1z1R3C5X628k7fec9+vbtW2Hs1ltvzcKFC3P00UenYcOG5eaKi4u/85lV5ZlnnskXX3yR8847L/vvv391t8MPhBAzAAAAAAAAAAAAwPesX79+FcZGjhyZhQsX5phjjkmrVq2qoas1Y9asWUmSDTbYoJo74YekoLobAAAAAAAAAAAAAOD/9OnTJ0VFRVm8eHEGDhyYbt26pW3btunfv3+SZOHChRkyZEiOPvro7Lbbbmnbtm26dOmSX/3qV5kyZUqlexYVFaVPnz75+OOP87vf/S677LJL2rZtm/322y/33ntvhfrS0tKMHDkyvXv3TpcuXbLttttm9913zwknnJCHHnooSTJx4sQUFRVlwIABSZKjjz46RUVFKSoqysSJE8v2mjdvXq666qrsu+++adeuXTp27JhjjjkmEyZMqHDuiBEjUlRUlBEjRuTJJ59Mnz590rFjxxQVFX3n98raxU3MAAAAAAAAAAAAAGuhX//613nxxRez2267Za+99sr666+fJHnzzTfz5z//OTvssEP22GOPNGzYMB988EEee+yxjB8/PoMGDcpuu+1WYb8FCxbk8MMPT+3atdOtW7csXrw4Y8aMyW9/+9sUFBSkZ8+eZbXXXHNNBg8enFatWmXfffdNgwYNMnv27Lz44osZM2ZMunfvnpYtW6Zv376ZNGlSJk2alJ49e6Zly5ZJUva/06dPT58+fTJ9+vTssMMO2XXXXfPZZ5/l8ccfz4knnpiLL744hx56aIVeH3nkkYwfPz677bZbevfunRkzZnwfr5hqJMQMAAAAAAAAAAAAsBaaPn16HnzwwTRp0qTc+JZbbpknn3yywvjMmTNz8MEH57LLLqs0xPzqq6/m4IMPzsUXX5yaNWsmSY455pgccMABueGGG8qFmO++++40b948o0aNSp06dcrt8/HHHydJWrVqlX79+mXAgAFlIeYdd9yxXG3//v0zY8aMXH311dlvv/3KxhcsWJA+ffrkv//7v9O1a9c0bdq03Lonnngi119/faXPwY9DQXU3AAAAAAAAAAAAAEBFv/nNbyoElZOkQYMGlY5vuOGG2WefffLWW29VenNxnTp1cv7555cFmJNkq622SocOHfLmm2/m008/LVdfWFhYrnaFys6uzKuvvppJkyZl7733LhdgTpKGDRumX79++eKLL/LII49UWLvnnnsKMP/I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AAAAAAAAAAAArEUKC8vHO++55578/ve/T+3atdO1a9dsuOGGmTZtWoYPH57HHnssw4YNS4sWLdKwYcP07ds3I0eOzPTp09O3b9+yPVq2bPmd+3r33Xdz6KGHZrPNNsv++++fzz//PPXr1y+bnz59eg455JBsvPHGOfDAAzN//vw89NBDOe2003LzzTenS5cuq9y/uLg4ffv2zcCBA9OyZcv07NmzbK5z585l31999dUZPHhw1ltvvfTo0SN169bN+PHjc/XVV2fChAm58cYbU7t27a99nuHDhydJTj311BQUVH4vcEFBQU499dScfPLJGTZsWE499dQkyU477ZTRo0fnmWeeyWabbVZW/8wzzyRJpkyZki+++CLrrLNOkmTy5MlZunRpdtpppwpn/P3vf8+4ceOy6667pnfv3nnzzTfzxBNP5MUXX8zo0aPTpEmTstoFCxbkmGOOySuvvJJtttkmBx10UJYvX54JEybkrLPOyhtvvJEzzjijwhnPP/98Bg8enI4dO+aggw7K3LlzU6tWra99R98nIWYAAAAAAAAAAACAajZ58uS89dZbqVWrVtq1a1c2/vbbb+eiiy5Ky5Ytc/vtt6d58+Zlc88880yOP/74XHrppbn22mvTsGHD9OvXL5MmTcr06dPTr1+/NdpjSUlJTjnllJx55pnlxlfc6Dtp0qT069evXHi6R48eOfHEE3PjjTeuVoi5uLi4LMRcWf9TpkzJ4MGDs9FGG2X48OFp1qxZkuSss85K37598/jjj+emm27Kr371q1We9cEHH2TGjBkpLCzMjjvuuMraHXfcMYWFhZkxY0ZmzpyZDTfcsOxZnnnmmRx++OFJkrfeeiuzZs3Kz3/+8zz11FN57rnnykLLK8LNlb2DsWPH5sYbbywXcL7qqqty/fXX5957781JJ51UNv6HP/whr7zySs4+++xy41988UVOO+20DB48OPvss0+Ki4vLnTFhwoT813/9V3r37r3KZ61KlcfGAQAAAAAAAAAAAPjeDBgwIAMGDMg111yT008/Pccdd1xKS0tz3nnnZYMNNiiru+uuu7JkyZJccMEF5QLMyZe3AXft2jWPP/54Pvnkk++956ZNm5YLKP+7li1blt1UvMKuu+6aFi1a5IUXXlgjPdx7771Jvrw9eUWAOfny9urzzjsvBQUFZTcsr8rs2bOTJI0bN8666667ytp11103jRs3TpJ8+OGHSZKNN944LVu2zMSJE1NaWprk/4LKv/71r1OzZs2yn1fM1a1bN9ttt12F/bt3717hhuZDDz00SfLiiy+Wjc2dOzcPPPBA2rZtWy7AnCTrrLNOzjnnnJSWlubBBx+scEZxcfFaFWBO3MQMAAAAAAAAAAAAUOUGDhxY7ucaNWrk0ksvzUEHHVRu/Pnnn0/y5S3HXw20rjBnzpwsW7Ys77zzTtq2bfu99ZskrVu3Tu3atVc5X7NmzQrjG264YdlzfFevvPJKkspvNN58882z4YYb5v3338/ChQvToEGDNXLmynTp0iX33ntvpk6dmjZt2mTixIlp1qxZtt9++2yzzTZlIeaPP/44b7zxRn7+85+nVq1aFfap7J/bRhttlCSZP39+2diLL76YZcuWpUaNGhkwYECFNUuXLk3y5Y3Q/+6rt3uvLYSYAQAAAAAAAAAAAKrYa6+9liRZtGhRnn/++VxwwQW58MIL06JFi3K38s6bNy9JcuONN65yv0WLFn1vva7QtGnTVc43bNiw0vHCwsIsX758jfSwcOHCJCl3C/NXNWvWLDNmzMiCBQtWGWJe8Szz5s3L559/vsrbmD///POyfw5fvSV7p512yr333ptnnnkmrVu3zsSJE7PbbruVzQ0ZMiQLFy7Ms88+m9LS0gq3La9Q2XsrLPwy4vvV97aihxdffLHSQPsKn3766Uqfd20ixAwAAAAAAAAAAABQTerWrZudd945gwYNSq9evdK/f/+MGTMmderUSZLUr18/SVJSUlL2/XdVo0aNslt7/92CBQtWua66rQgmf/TRR9lkk00qzM+ePbtc3cq0aNEiG220UT744INMnDgxu++++0prJ06cmKVLl6ZFixbZcMMNy8ZX3Ab99NNPp0uXLpk3b15ZULlLly4ZPHhwJk6cWHYjc2W3R38TK57p2GOPzfnnn/+N1q4N/+z+XUF1NwAAAAAAAAAAAADwU9e6desccsghmTlzZm655Zay8e233z5J8o9//GO19yoo+DIeumzZskrnGzVqlJkzZ1YYX7ZsWV599dXVb/p7UlBQsNLei4uLk3wZLP5306ZNy8yZM9OqVauV3gr9VQcffHCSZPDgwSktLa20Zvny5Rk8eHCS5NBDDy0316xZs2y11VYpKSnJ+PHjk6QsxNyhQ4fUrl07zzzzTJ599tk0atQobdq0+dqeVqVdu3YpKCj4Rr8W1mZCzAAAAAAAAAAAAABrgdNOOy21a9fOTTfdlPnz5ydJjjzyyNSqVSuXXXZZ3n777QprFi9eXCHU2rhx4yTJjBkzKj1n2223zYwZMzJhwoRy44MGDcr06dPXwJN8N40bN640ZJ0kBx10UJIve/3444/LxpctW5Yrrrgiy5cvLwsnf53jjjsuW265ZUpKSnLBBRfk888/Lzf/+eef5z//8z9TUlKSrbfeOscee2yFPbp06ZLPPvsst912WzbbbLNstNFGSZJ1110322+/fR5++OG8++676dy5c1m4/Ntaf/31s//+++ell17KtddeW2nQ+91338177733nc6pKoXV3QAAAAAAAAAAAAAASfPmzdO7d+/cdtttGTJkSM4666xsueWWufTSS3PBBRekR48e2XXXXbPZZptl6dKlmTFjRkpKSrLeeutlzJgxZfvstNNOGTNmTPr165fdd98966yzTlq0aJFf/vKXSZITTjghEyZMyGmnnZbu3bunUaNGmTJlSt5///107tw5kyZNqqY38H/9jx49Or/61a/Spk2bFBYWplOnTunUqVM6dOiQE088MUOGDEmPHj3SrVu31KlTJ+PHj8/rr7+ejh075oQTTlitc+rVq5chQ4bk1FNPzb333psnn3wyu+22W5o1a5aPPvooTzzxRGbPnp3i4uJcd911qVOnTqW93n777ZkzZ05+8YtfVJhb8S5X3ND8Xf3+97/PtGnT8j//8z954IEH0qFDhzRt2jQffvhh3nzzzbz44ou5+uqrs/HGG6+R875PQswAAAAAAAAAAADA2uHYUdXdQbU75ZRTMnz48AwdOjTHHHNMmjZtmgMPPDCtW7fOzTffnIkTJ2bChAmpW7duNthgg3Tr1i377rtvuT0OOeSQzJgxI6NHj86QIUOydOnSdO7cuSzEvNNOO+Xaa6/Ntddem9GjR6du3brZeeedc80112TAgAHV8NTlXXDBBalRo0aeeeaZPPHEE1m+fHn69u2bTp06JUnOOeectGnTJrfffnvuu+++LF26NJtssklOP/30HH/88aldu/Zqn9WiRYvcc889GTlyZB566KE89thjWbhwYRo0aJCioqL8+te/Ts+ePVOrVq1K16+4YXn58uXp0qVLubmddtopf/nLX5Kkwty3Vb9+/QwdOjTDhg3LqFGj8uijj+aLL75I06ZNs+mmm+b888/PzjvvvEbO+r7VKC0tLa3uJqheJSUlSZKOHTtWcycAa6epU6cmSYqLi6u5EwB+zHzeAFAVfN4AUFV85gBQFXzeAFAVfN4ArNp3yaAWrOlmAAAAAAAAAAAAAABWRYgZAAAAAAAAAAAAAKhSQswAAAAAAAAAAAAAQJUSYgYAAAAAAAAAAAAAqlRhdTcAAABAUlxcXN0tAAAAAAAAAECVcRMzAAAAAAAAAAAAAFCl3MQMAAD84E07+pjqbuE72/S2W6u7BQAAAAAAAACoMm5iBgAAAAAAAAAAAACqlBAzAAAAAAAAAAAAAFClhJgBAAAAAAAAAAAAgColxAwAAAAAAAAAAAAAVCkhZgAAAAAAAAAAAACgSgkxAwAAAAAAAAAAAABVSogZAAAAAAAAAAAAgO/NgAEDUlRUlIkTJ1Z3K6xFhJgBAAAAAAAAAAAAqkhRUVG5r+Li4nTu3Dl9+vTJiBEjUlpaWmHNxIkTU1RUlAEDBlR5vw888EBZrxMmTKjy87+roqKi9OnTp7rboBKF1d0AAAAAAAAAAAAAQJIc/8jx1d1CpW7qdtMa37Nv375JkqVLl2batGkZO3ZsJk2alJdeeim///3v1/h539awYcNSo0aNlJaWZtiwYdlll12quyV+JISYAQAAAAAAAAAAAKpYv379yv1cUlKSo446KnfeeWeOO+64bLzxxtXU2f956623Mnny5Oy8886ZP39+HnvssXz00Udp2rRpdbfGj0BBdTcAAAAAAAAAAAAA8FPXsWPHbLHFFiktLc3LL79cNt6/f/8cffTRSZKBAwemqKio7GvixIlldYsXL87111+f/fffP9ttt106dOiQI444Ig899NC37mn48OFJkl69eqVXr15ZsmRJRowYsdL6l156KSeccELat2+fDh065Nhjj82UKVNWecYzzzyTE044IZ07d07btm3TrVu3XHnllVm4cGGF2j59+qSoqCiLFy/ONddck65du6Zt27bZa6+9MnDgwCxevLisdsSIESkqKkqSTJo0qdx7GzBgwLd5HaxhbmIGAAAAAAAAAAAAWIsUFv5fvHOvvfZKkowcOTKdO3dO586dy+ZatmyZ5MsA8wknnJBJkyZliy22yBFHHJHPP/88jzzySM4444y8+uqrOfPMM79RD4sXL87IkSPToEGD/OIXv8jnn3+eyy+/PPfcc09OOumk1KhRo1z9c889l+OOOy5LlizJL37xi2y66aaZOnVq+vTpky5dulR6xt/+9rdcdNFFqVOnTvbZZ5+sv/76mTRpUm644YY8/vjjueuuu9KwYcMK637zm9/kxRdfzD777JPCwsKMGzcuAwYMyEsvvZRBgwalRo0aKS4uTt++fTNw4MC0bNkyPXv2LFv/1XdI9RFiBgAAAAAAAAAAAKhmkydPzltvvZVatWqlXbt2ZeN77bVXGjRoUBZi7tevX4W1N998cyZNmpTddtstgwYNKgtB9+3bN4ccckgGDx6cPfbYIx06dFjtfv73f/83c+fOzWGHHZZ111036667brp27ZpHHnkkzz77bHbaaaey2tLS0vz2t7/N559/nmuvvbYseJ0kt956a/7whz9U2H/69On57//+79StWzfDhw/PlltuWTZ30UUX5a677sqf/vSnXHLJJRXWvvXWWxk9enQaNWqUJDnjjDNy9NFH5/HHH8/999+fX/7ylykuLk5xcXFZiLmy90b1KqjuBgAAAAAAAAAAAAB+agYMGJABAwbkmmuuyemnn57jjjsupaWlOe+887LBBht8o73uvffe1KhRI/379y93i/P666+fU089NUkyfPjwb7TnsGHDkqTcDcYrvr/77rvL1T733HN5++2306lTp3IB5iQ56qijsskmm1TY/4EHHsiSJUty1FFHlQswJ1+GkuvVq5f7778/ixcvrrD21FNPLQswJ8k666xTdtP0vffe+00ek2rkJmYAAAAAAAAAAACAKjZw4MByP9eoUSOXXnppDjrooG+0zyeffJJp06alefPmFcLASdKlS5ckydSpU8vGxo4dW+7nJCkuLi4LIE+bNi0TJ07M5ptvnvbt25fV7LrrrmnWrFnGjh2bjz/+OE2aNEmSvPLKK0mSTp06VTi/Zs2a6dixY959991y4yvWrOjvqxo1apQ2bdqU3U7dunXrcvOdO3eusKZjx46pWbNmhedi7SXEDAAAAAAAAAAAAFDFXnvttSTJokWL8vzzz+eCCy7IhRdemBYtWmSnnXZa7X0++eSTJEmzZs0qnV9xq/OCBQvKxsaOHZuRI0eWq+vZs2dZiHnYsGEpLS1Nr169ytUUFhZm//33z0033ZSRI0fmhBNOSJIsXLgwSdK0adNKe6hsfMWalfW9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t9126dy5c84444zMmjVrle+AtVthdTcAAAAAAAAAAAAA8FPy0Ucf5bHHHstmm22WDh06pH79+rnpppty9913p3v37uVqx4wZkzPOOCO1atVK9+7d06xZs5SUlKR3794pKiqqdP+rr746gwcPznrrrZcePXqkbt26GT9+fK6++upMmDAhN954Y2rXrl1uzeLFi3Psscdm4cKF2W+//bJkyZI88sgjufTSS/P222/nwgsvTJJ07tw5Rx99dG677ba0bt06e+21V9kexcXFq3zuF154Iccdd1w+/fTTdO3aNVtttVXeeuutPPDAAxk3blxuvvnmtGvXrsK6O++8M4899li6du2aTp065YUXXshDDz2UV199Nffff3+FZ+GHQYgZAAAAAAAAAAAAoAqNGDEiS5YsSa9evZIkW2+9dbbZZptMnDgx06ZNy6abbpok+fTTT3PhhRemoKAgd9xxR7bddtuyPf7whz/k1ltvrbD3lClTMnjw4Gy00UYZPnx4mjVrliQ566yz0rdv3zz++OO56aab8qtf/arcutmzZ2fjjTfOqFGjykLB/fr1y8EHH5w777wz3bt3T6dOnbLjjjumZcuWue2221JcXJx+/fqt1jOXlpbmvPPOyyeffJI//elPOeCAA8rmHnrooZxxxhk599xz89BDD6WgoKDc2vHjx+eee+4pF9o+66yzMmrUqIwdO7ZC8JsfhoKvLwEAAAAAAAAAAABgTSgtLc3w4cNTUFCQX/7yl2XjvXr1SmlpaYYNG1Y2Nm7cuMybNy89evQoF2BOvgwYN2jQoML+9957b5Lk1FNPLQswJ0lhYWHOO++8FBQUZPjw4ZX2dtZZZ5W71bhx48Y57bTTknwZvP4unnvuubz11ltp3759uQBzknTv3j0dO3bM22+/nZKSkgpr+/TpU+HW6UMOOSRJ8uKLL36nvqg+QswAAAAAAAAAAAAAVeTZZ5/Nu+++m5133jnNmzcvG+/Ro0dq1aqVkSNHZsmSJUmSV155JUnSqVOnCvs0aNAgxcXFFcZXrOnSpUuFuc033zwbbrhh3n///SxcuLDcXGFhYdq3b19hTefOncvt+22tWL/jjjtWOr+i38rO+fcAd5JstNFGSZL58+d/p76oPkLMAAAAAAAAAAAAAFXk7rvvTvLlzctf1bhx43Tt2jVz5szJuHHjkqQsaNy0adNK96psfMWar97C/FUrxhcsWFBufL311kvNmjVXWv/voedvasX6DTbYYJV9VXZOZTdOr+h1+fLl36kvqk9hdTcAAAAAAAAAAAAA8FPw8ccfZ+zYsUmSM888M2eeeWaldcOGDcs+++xTFt796KOPKq2rbPyrazbZZJMK87Nnzy5Xt8LcuXOzbNmyCkHmldV/UyvWr9hvZX3Vr1//O53DD4cQMwAAAAAAAAAAAEAVGDlyZJYsWZJtttkmxcXFldY89thjefrpp/Pee++lTZs2SZLJkyfn4IMPLle3cOHCTJ06tcL64uLivPzyy5k4cWKFEPO0adMyc+bMtGrVKg0bNiw3t3Tp0kyZMiU77LBDufFJkyYlSVkvyf/dgrxs2bLVeeyyvr6637+bOHFikmSbbbZZ7T35YRNiBgAAAAAAAAAAAKgCw4YNS5JcdNFFadeuXaU1f/7znzNo0KDcc889Ofnkk9OoUaOMGjUqRx11VLbddtuyugEDBmThwoUV1h900EG55557MmjQoOy5555p0qRJki8Dx1dccUWWL19eIRC9wlVXXZVbb701tWvXTpLMmzcvgwYNSpL06tWrrK5hw4apUaNGPvjgg9V+9o4dO2bzzTdPSUlJxowZk3322adsbsyYMfnHP/6RzTbbLB07dlztPflhE2IGAAAAAAAAAAAA+J5NnDgx77zzTrbeeuuVBpiT5OCDD851112Xe++9N/369cvFF1+cM844I0ceeWS6d++eZs2apaSkJG+88UY6deqUyZMnl1vfoUOHnHjiiRkyZEh69OiRbt26pU6dOhk/fnxef/31dOzYMSeccEKFc5s1a5bFixenR48e6dq1a5YuXZoxY8Zk9uzZOeKII9KpU6ey2nr16mW77bbLP/7xj5x11lnZfPPNU1BQkK5du6Z169aVPleNGjVyxRVX5LjjjssZZ5yRUaNGZYsttsjbb7+dsWPHpl69evnjH/+YgoKCb/mG+aERYgYAAAAAAAAAAADWCpvedmt1t/C9WXEL8yGHHLLKulatWmXnnXfOU089lccffzz77LNPGjRokIEDB+bhhx9O7dq1s8MOO+Rvf/tbbrjhhgoh5iQ555xz0qZNm9x+++257777snTp0myyySY5/fTTc/zxx5fdtPxVtWvXzi233JKrr746o0ePzty5c7Pxxhvn5JNPTp8+fSrU//GPf8xll12WCRMmZPTo0SktLc2GG2640hBzkmy33XZlt0Q/88wzefzxx7Peeutlv/32y2mnnZYtttji614jPyI1SktLS6u7CapXSUlJkriCHWAlpk6dmiQpLi6u5k4AWJlpRx9T3S18Zz/m/zMGgLWHP98AUFV85gBQFXzeAFAVfN7wU9G1a9ckyWOPPVbNnfBD810yqO7cBgAAAAAAAAAAAACqlBAzAAAAAAAAAAAAAFClhJgBAAAAAAAAAAAAgCpVWN0NAAAAAAAAAAAAAFB9HnvssepugZ8gNzEDAAAAAAAAAAAAAFVKiBkAAAAAAAAAAAAAqFJCzAAAAAAAAAAAAABAlRJiBgAAAAAAAAAAAACqlBAzAAAAAAAAAAAAAFClhJgBAAAAAAAAAAAAgColxAwAAAAAAAAAAAAAVCkhZgAAAAAAAAAAAACgShVWdwNV4YQTTsiECRPKfr7sssvSq1evr1335JNPZsSIEfnnP/+Zjz76KPXr18+mm26affbZJ4ceemjq1q272j1MmTIlw4YNy+TJkzN79uyss846adWqVfbaa6/07t07TZo0We29Xn/99dx999156qmnMmvWrBQUFKRFixbZfffdc/jhh6dly5arvRcAAAAAAAAAAAAAVLUffYh55MiR5QLMq2Px4sXp379/Ro8eXW78448/zscff5wpU6bkjjvuyIABA9K6detV7lVaWprLL788t956a0pLS8vGP//888yfPz8vv/xy7rjjjlx55ZXZaaedvra3G2+8Mddcc02WLFlSbvz111/P66+/njvvvDOXXHJJ9ttvv2/wxAAAAAAAAAAAAMBPRdeuXZMkjz32WDV3UjUmTpyYo48+On379k2/fv2qux3+fz/qEPOcOXNy+eWXJ0nq1q2bRYsWrda68847Lw899FCSpHHjxjnssMOy9dZbZ+7cuXnggQfywgsv5N13382JJ56Y4cOHZ6ONNlrpXldddVVuueWWsh4OOuigtGvXLosWLcqjjz6ap556Kh999FFOO+203HnnnSkuLl7pXnfddVf++Mc/Jklq1aqVAw44IJ07d86SJUsyYcKEPPLII/n0009z7rnnpkGDBtltt91W63kBAAAAAAAAAACAqlFUVPS1Nbfddlt23HHHb31Gnz59MmnSpLz22mvfeg/4vv2oQ8yXXHJJ5s2blzZt2mSrrbbKAw888LVrxo4dWxZgbtGiRe644460aNGibP7II4/MBRdckBEjRmT27Nm57LLL8j//8z+V7vXKK69kyJAhSZIGDRrk9ttvL3dzc+/evTNgwIAMHDgwixYtyu9+97sMHz48NWrUqLDXhx9+mCuuuCJJUlhYmOuvvz4777xz2fwhhxySESNG5Pzzz8/SpUvz+9//Po888kjWWWed1XhTAAAAAAAAAAAAUP3uu/q56m6hUr88s8Ma37Nv374rnWvZsuUaP++nrF27dnnooYey3nrrVXcrfMWPNsQ8bty4PPzwwykoKMjFF1+cO+64Y7XWDRw4sOz7iy66qFyAOUkKCgpy4YUX5tlnn82MGTPyyCOP5PXXX8/WW29dYa9rr702paWlSZIzzjijXIB5hb59++bJJ5/MCy+8kBdffDFPPPFE9thjjwp1Q4YMyWeffZYkOeaYY8oFmFfo1atXnnjiiYwZMyYffPBB7rnnnhx55JGr9dwAAAAAAAAAAABA1enXr191t/CTUadOnWy55ZbV3Qb/pqC6G/g+fPLJJ/mv//qvJF/enLztttuu1rp33nknU6dOTZJsttlm2X333SutW3fddXPIIYeU/fzwww9X2sOTTz6ZJKlfv3569epV6V41atTIUUcdVfbzilugv6q0tDRjxowpq+/Tp89Kn+Grc5XtBQAAAAAAAAAAAPxw9O/fP0VFRXn//fcrzE2cODFFRUUZMGBAkuT9999PUVFRJk2alCQpKioq+6ose7ho0aJcccUV2WOPPdK2bdv84he/yPXXX192getXjRgxIv369cuee+6Zdu3apUOHDundu3fuv//+Svvu06dPioqKsnTp0lx33XXZe++907Zt2+y+++7505/+lMWLF1dYM3bs2Jx99tnp1q1btt9++2y//fbp1atXbrvttixfvrxC/UcffZQrrriirH6HHXZIt27d0r9//7z33nsrfU8rvPTSS/nv//7vHHDAAencuXO23Xbb7L333rn88sszf/78Sp+LNedHeRPzH//4x8yaNSsbbrhhTj/99NVeN2HChLLvd9lll1XW7rrrrvnLX/6SJBk/fnx+85vflJufPHly2W+wTp06pU6dOqvca4Xx48dXmH/jjTcya9asJMnPfvazbLTRRivdq0OHDqlfv34++eSTPPfcc/nkk09Sv379VT4LAAAAAAAAAAAA8MPXsGHD9O3bNyNHjsz06dPTt2/fsrmWLVuWq12yZElOOOGEfPjhh9ltt91Ss2bNjB07NldddVUWL15cbm2SXHTRRdlqq63SqVOnNGvWLPPmzcsTTzyRc889N2+//fZK85pnnXVWSkpKsuuuu2b33XfPk08+mSFDhuTjjz/OZZddVq72yiuvTEFBQdq1a5fmzZtn4cKFefbZZ3PppZfmxRdfzJ/+9Key2s8++yyHH3543n333fz85z9P165dU1pamhkzZmTcuHHp1q1bNt5441W+r2HDhmXs2LHp1KlTdt555yxfvjwvv/xybr755jz55JMZNmyYDOb36EcXYp48eXKGDRuWJPnd7373jX7xvP7662Xfb7PNNqusLS4uTs2aNbNs2bK8+eabKS0tTY0aNcrm33jjjdXeq0mTJmnZsmWmT5+ejz/+OHPmzMn666//rfYqKChImzZtMmnSpCxfvjxvvfVW2rVrt8o1AAAAAAAAAAAAQNX691uBV1hnnXVy8sknf6s9GzZsmH79+mXSpEmZPn16+vXrt9LaDz/8MK1bt87NN9+cddddN0nSt2/fdOvWLbfccktOOeWU1KpVq6x+1KhR2WSTTcrtsXjx4px00km54YYbcvjhh6d58+YVznnvvfcyatSoNG7cOElyxhln5MADD8x9992XM888M82aNSurvf766yucsXz58px//vm57777ctRRR2W77bZLkjzzzDN59913c8wxx+S3v/1thb4qu+n5351yyim58MILU7NmzXLjw4cPz3/+53/mzjvv/Nb/LPh6BdXdwJr0xRdf5D//8z9TWlqaX/ziF9lrr72+0fp33nmn7Pt//xsH/66wsLDsN9uiRYvKbkpe4e23317tvZKkRYsWla5d03sBAAAAAAAAAAAA1W/gwIGVfl1//fVV1sN//ud/lgWYk2T99dfPnnvumYULF1bIH/57uDhJateunSOPPDJLly7NM888U+kZZ599dlmAOUnq1q2b/fffP8uXL89LL730tWcUFBTk6KOPTpKMHz++wvxX+/9qX6tzCW7Lli0rBJiT5OCDD079+vUzYcKEr92Db+9HdRPzwIED884776RevXr53e9+943XL1y4sOz79dZb72vrGzdunBkzZiRJFixYkA033PA77VXZ2jW916pMnTp1tWsBfko+++yzJP49CbA2Ki4uTvLlXyz8sfB5A8D3yZ9vAKgqPnMAqAo+bwCoCj5vqs6K//b36Vr+3/7W5K+F++67b7XOmTdvXpLkX//6V4VM4LRp05Iks2fPLrfm008/rbDPVy1evDh169bNokWLKtSsuH35hRdeyLJly8rGZ8+enREjRuSFF17I7NmzK9x0/OKLL6aoqKhCD7Vq1VppH1OnTi2XvVywYEHuu+++lJSUZNasWfn888/L1b/22mtlezVq1Cjrr79+rr/++kyaNCkdO3ZM69ats/nmm1cIJq/sPS1dujSPPPJIJkyYkPfeey+LFi3K8uXLy+bfe+89v/+/Rz+aEPPUqVNz0003JfnyqvHKriT/Ol8NPqyzzjpfW//VmhW/2daGvb76twr+fS8AAAAAAAAAAACAevXqVTpeUFCQJOXCvDNnzsw555yTTz/9NMXFxdl+++1Tt27dFBQU5MMPP8zjjz+eJUuWVLpfZTciV3bGJ598knPOOSezZs3Kz372s+yxxx5p0KBBCgoK8umnn2bUqFHlzqhbt26uuOKK3HXXXZk8eXKmTJmSJGnYsGH23XffHHLIISksXHVM9sorr8yzzz6b5s2bp3PnzllvvfXK1jz44IMrfSbWjB9FiHnZsmW54IILsnTp0my77bY58sgjq7ulH6QVf5MFgPJW/G0q/54EWHvVrVu3ultYY3zeAPB98ucbAKqKzxwAqoLPGwCqgs+bqldvLf9vf2vy18Lq7rXeeuslSTbffPNsuumm5eamT5+eJGnWrFm5/VYElFd2Ru3atVc636xZsyTJpptuWjY/fPjwLFy4MJdddll69epVrn7UqFF5/PHHv1EPK35vtWjRomz+xhtvzKxZs9K3b9/069evXP2UKVMyatSoNG7cuMJ+u+66a0pLS/Ovf/0rzz77bO64447cfffdadKkSU4//fQkX97w/O/v6cUXX8yzzz6bnXfeOTfccEO5wPPy5ctz//33p3bt2n7/f42SkpJvvbZgDfZRbW666aa8/PLLKSwszH//93+XJfS/qa8GH7744ouvrf9qzb//jYTq3Our16ev7G9KAAAAAAAAAAAAAGu/Ro0aJUk++OCDCnMvvvhipWtW5CiXLVu2RnqYNm1akmTvvfeuMDdp0qTv/YzJkyevcm2NGjXys5/9LH369MnNN9+cJBk3btwq17z77rtJkq5du1a4sfmFF14ol8Xk+/GDDzFPmzYtAwcOTJIcc8wxad269bfeq0GDBmXfz50792vr582bV/Z9w4YN19heX127pvcCAAAAAAAAAAAAfjjatWuX5MvbkL/qtddey2233VbpmsaNGydJZsyYsUZ6aNmyZZKKgeXx48fnnnvuWSNntGrVqtIzXnnllQwePLhC/RtvvJGPPvqowviKsXXXXXeV563smebMmZOLL7549RvnWyv8+pK124MPPpjPP/88NWrUSGFhYf76179WWvfaa6+Vff/4449n5syZSZJddtml7Df4ZpttlokTJyb5vyvWV2bp0qWZNWtWki9vSm7evHm5+c0337zs+6/bKyn/L4qvrl3TewEAAAAAAAAAAADVb8CAASud22uvvVJcXJwk2XPPPbPZZptl1KhRmTlzZtq1a5cPPvgg48aNy5577pmHH364wvqddtopY8aMSb9+/bL77rtnnXXWSYsWLfLLX/7yW/V6xBFHZMSIEfnNb36Tbt26ZYMNNsgbb7yR8ePHZ999981DDz30rfb9qgMPPDA33nhj/vCHP2TixInZdNNNM23atPz973/PL37xiwpnPPXUU/nTn/6U7bffPptttlnWX3/9zJw5M+PGjUtBQUFOOOGEVZ637bbbpkOHDnn00UfTu3fvdOjQIXPmzMmTTz6ZzTffPBtssMF3fiZW7QcfYi4tLS3738qS9pV59NFH8+ijjyb5MoC8IsS89dZbl9W8/PLL6dWr10r3mDp1atk161tuuWVq1KhRbv5nP/tZub1W5eOPPy4LJzdp0iTrr7/+t95r+fLleeWVV5J8eR38Fltsscp6AAAAAAAAAAAAWFv88swO1d1ClRk4cOBK51q2bFkWYl5nnXVyyy235IorrsjTTz+dF198MT/72c9y1VVXpVGjRpWGmA855JDMmDEjo0ePzpAhQ7J06dJ07tz5W4eYW7dundtuuy1//vOf88QTT2Tp0qVp3bp1Bg4cmAYNGqyREHPz5s1zxx135Morr0xJSUkmTJiQLbbYIhdeeGF22mmnCmfsuuuu+eCDDzJ58uSMGzcun3zySTbYYIP8/Oc/z7HHHpsOHVb9a6lmzZoZNGhQ/vznP+fJJ5/M0KFD07x58xxyyCE59dRTs99++33nZ2LVfvAh5jVpl112Kft+woQJq6wdP3582fe77rprhfnOnTundu3aWbx4cSZPnpzPP/98pVeTf91eP/vZz7Lhhhtm5syZeeONNzJz5sxsuOGGle713HPP5ZNPPkmSdOjQIfXr11/lcwAAAAAAAAAAAABV57XXXvvGazbaaKP8+c9/Xu39atasmTPPPDNnnnlmpWsee+yxlZ7Vr1+/9OvXr8J4hw4dctttt612D0OHDl3pGb169ar0otmtttoq11133WqdseWWW+b8889f6RlfteOOO1baY+PGjXPRRRdVumZV74g1o6C6G/iu+vXrl9dee+1rv3r27Fm25rLLLisbP/bYY8vGN9tss7Rp0yZJ8s477+SJJ56o9Mwvvvgiw4cPL/t53333rVBTr1697L777kmSTz75JCNGjKh0r9LS0txxxx1lP3fv3r1CTY0aNbLPPvuU1a/qN/ZX5yrbCwAAAAAAAAAAAACq2w8+xLym/b//9//Kvv+v//qvzJgxo9z88uXLy41369YtW2+9daV7nXbaaalRo0aS5Oqrr86rr75aoebaa6/NP//5zyTJtttumz322KPSvY4//vjUqVMnSXLLLbfkmWeeqVAzYsSIjBkzJsmXf+vi4IMPXtWjAgAAAAAAAAAAAEC1KKzuBtY2e+21V7p3756HHnoo06dPT8+ePdO7d+9svfXWmTdvXu6777688MILSZJmzZqt8iryNm3a5MQTT8wNN9yQhQsX5vDDD8/BBx+cdu3aZdGiRXn00UczYcKEJEndunVzySWXrHSv5s2b57zzzstFF12UpUuX5qSTTsqBBx6YTp06ZdmyZXnyySfzyCOPJEkKCwtz8cUXZ5111lmDbwYAAAAAAAAAAAAA1gwh5kpcccUVqVGjRkaPHp158+bluuuuq1CzySabZMCAAdloo41WuddZZ52VxYsX57bbbsuiRYty2223VahZf/31c9VVV6W4uHiVex1++OFZtGhRrrnmmixZsiT33HNP7rnnnnI19erVyyWXXJLddtttNZ4UAAAAAAAAAAAAAKqeEHMlateunauvvjq//OUvc++99+af//xn5syZk3r16mWzzTbLPvvsk0MPPTR169b92r1q1KiR3/72t9l3330zbNiwTJ48OR9++GHWWWedbLzxxtlzzz1z+OGHp0mTJqvV2wknnJBdd901f/vb3/LUU0/lww8/TI0aNdKyZcvsvvvuOfzww9OyZcvv+goAAAAAAAAAAAAA4HvzkwkxX3755bn88su/0Zrddttt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L7fmiiuuyGeffbbGe4HqIMQMAAAAAAAAAAAAUMX69etXYeyjjz7KJZdckjFjxuS4447Lvffem/XXX79svkWLFlXZInyvhJgBAAAAAAAAAAAA1gJNmzbNNddck48//jiTJk3KddddlwsuuKBsvk+fPpk0aVJee+21srHS0tLcd999ufvuu/POO+/k008/TZMmTbLVVlvloIMOSvfu3ctqu3btmiS5//77c8011+R///d/M2/evGy88cbp3bt3+vTpkxo1alTo66GHHsodd9yRV199NUuWLMmmm26aHj165Ljjjkvt2rXL1b766qu5/vrr8/zzz+fDDz9M/fr1s9FGG2WHHXbIueeem1q1aiVJZs2aleHDh2fChAl57733Mn/+/DRu3Dg77rhjTj311Gy11VZr9N2y9imo7gYAAAAAAAAAAAAA+FJBQUFOO+20JMno0aNTWlq6yvprrrkm/fv3z+zZs7PvvvvmuOOOy84775xZs2ZlzJgxFeoXL16cY489NhMmTMh+++2XQw89NAsWLMill16aiy++uEL91VdfnTPOOCNvvvlmevTokSOPPDKlpaW5+uqrc8IJJ2Tx4sVlta+++moOPfTQjBs3Ltttt12OO+647LvvvmnSpEnuuuuucrX/+Mc/csMNN6Rhw4bZe++9c8wxx2T77bfPI488kkMOOSSvvvrqt32F/EC4iRkAAAAAAAAAAABgLdKxY8cUFhZmzpw5ef/997PxxhuvtPbuu+9O8+bNM2rUqNSpU6fc3Mcff1yhfvbs2dl4440zatSosluU+/Xrl4MPPjh33nlnunfvnk6dOiVJpkyZksGDB2ejjTbK8OHD06xZsyTJWWedlb59++bxxx/PTTfdlF/96ldJkvvuuy9ffPFFrr322uy1117lzp0/f365/rp06ZKnnnoq9evXL1f36quv5vDDD8+VV16ZIUOGrO4r4wfITcwAAAAAAAAAAAAAa5HatWuncePGSZK5c+d+bX1hYWFq1qxZYbxJkyaV1p911lllAeYkady4cdntzyNGjCgbv/fee5Mkp556almAecV55513XgoKCjJ8+PAK+6+77roVxho1apSCgv+Lra6//voVAsxJ0rp16+y4446ZOHFilixZUmn//Di4iRkAAAAAAAAAAABgLVNaWrpadfvvv3+GDh2a7t27Z999902nTp3Svn37NGjQ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z87f//73cuNLlizJyJEj0759+5UGlfv06ZOioqJyY6WlpRk5cmR69+6dLl26ZNttt83uu++eE044IQ899FC52ldffTVnnnlmunbtmrZt26ZLly7p2bNnLr300ixZsqSsbsCAASkqKsrEiRPLrS8qKkqfPn3y8ccf53e/+1122WWXtG3bNvvtt1/uvffeSntevHhxBgwYkD333DNt27ZN165dc80112Tx4sVl+/HTUljdDQAAAAAAAAAAAAD81Oy33365/PLLM3z48Oy1115l44899ljmzJmTs88+O9OmTVvt/a655poMHjw4rVq1yr777psGDRpk9uzZefHFFzNmzJh07949yZcB5kMPPTQ1atRI165d06pVq3zyySd59913c9ddd+X0009PrVq1vva8BQsW5PDDD0/t2rXTrVu3LF68OGPGjMlvf/vbFBQUpGfPnmW1paWl6devX/7+979ns802y1FHHZWlS5dm5MiR+de//vUN3ho/JkLMAAAAAAAAAAAAAFWsfv366d69e0aOHJmZM2dmww03TJIMGzYs9evXz7777pvrrrtutfe7++6707x584waNSp16tQpN/fxxx+XfX/ffffliy++yLXXXlsuPJ0k8+fPr7B2ZV599dUcfPDBufjii1OzZs0kyTHHHJMDDjggN9xwQ7kQ8/3335+///3v2WGHHXLzzTendu3aSZJf//rXOfTQQ1f7GflxKajuBgAAAAAAAAAAAAB+ig499NAsW7Ys99xzT5Jk+vTpefrpp7P//vuvdpj4qwoLC8sCxV/VpEmTCmPrrrtuhbFGjRqloGD1oqV16tTJ+eefX+68rbbaKh06dMibb76ZTz/9tGz8vvvuS5KcfvrpZQHmJGnYsGFOO+201TqPHx8hZgAAAAAAAAAAAIBqsN1222XrrbfOiBEjsnz58gwfPjzLly//VrcT77///pk+fXq6d++eq666Kk8++WQWLlxYoa579+6pWbNm/t//+38599xzc9999+Xdd9/9xudtuummqV+/foXxFTdKL1iwoGxs6tSpKSgoSPv27SvUd+zY8RufzY+DEDMAAAAAAAAAAABANTn00EMzffr0PPnkkxkxYkS22WabtGnT5hvvc/755+f8889P3bp1c/311+ekk05Kly5dcuqpp2batGllde3atcsdd9yRLl265JFHHsl5552XX/zi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AABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKCoTh29gb2hUqlk0aJFWbx4cRYvXpwVK1akqakpn376aWpqanLIIYdk8ODBGT16dM4+++wcfPDBO51144035plnntnta7/99tu7te7111/P9OnTs3Dhwnz88cfp0qVLDj/88JxxxhkZP358evXqtdvXbGxszNNPP52GhoasWrUqtbW16devX0aNGpUJEyakf//+uz0LAAAAAAAAAAAAAErbLyLmTZs25Sc/+clOz2/cuDGrVq3K/PnzM2XKlEyePDlnnHFGkb1VKpXceeedefzxx1OpVFrt6bPPPsuSJUsyderU3HPPPTn55JN3Oe/RRx/Nfffdl82bN7d6v7GxMY2NjXnqqacyefLknHXWWXv9uwAAAAAAAAAAAADA3rBfRMzb9OnTJ9///vfzve99L/369UtdXV02bNiQd955J7Nnz87KlSvT1NSUq6++Og8//HBOOeWUdudNmjQpvXv3/lp7uvfee/PYY48lSbp165bzzz8/w4YNS0tLS+bOnZuGhoasWbMmV155ZZ566qkMGTJkp7OmTZuWu+++O0nSuXPnnH322TnxxBOzefPmLFiwIHPmzMn69etz/fXXp3v37jnttNO+1t4BAAAAAAAAAAAAYF/YLyLmzp075/nnn893v/vdna65+uqrM3ny5EybNi1btmzJ7bffnj/+8Y/tzj3llFNy+OGH7/G+li5dmkceeSRJ0r179zz55JM56qijqufHjx+f+++/Pw888EBaWlpy8803Z8aMGampqdlh1urVq3PXXXclSTp16pSHHnooI0aMqJ6/8MILM2vWrEycODFffvllbrnllsyZMyddunTZ4/0DAAAAAAAAAAAAwL5Q29Eb2Btqa2vbDZiT5IADDshNN92UHj16JElWrFiR9957b5/ua8qUKalUKkmSa665plXAvM1VV12VYcOGJUkWL16cl156qc1ZjzzySDZs2JAkueSSS1oFzNuMGzcuY8aMSZJ8+OGHmTlz5l75HgAAAAAAAAAAAACwN+0XEfPu6ty5cwYOHFh9/fHHH++zazU3N2fe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AAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgB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AAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAA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8sknkyRDhw7NhAkTagHye3XUUUfl2GOPTZJs2LAhs2bNarZm8xB6zZo127XXTTp37rxDs1avXr3VWQAAAAAAAAAAAADQ1tptxLx27dpcdNFFeeSRR5IkQ4YMyS233FK3/9vPj3zkI7XjF198sdn5rl271o5ff/31bc574403Wry23rMAAAAAAAAAAAAAoK21y4h53bp1ueSSSzJz5swkyaBBg3LrrbemS5cudbtHt27dascrV65sdv7ggw+uHb/yyivbnLdo0aIWr633LAAAAAAAAAAAAABoa+0uYl6/fn0uvfTS/O53v0uSDBgwID//+c+z77771vU+23racf/+/WvHTz/9dKuzVqxYUYuTe/TokZ49e77nWRs3bsyCBQuSJA0NDTnkkENaXQ8AAAAAAAAAAAAApbWriHnDhg257LLLMmPGjCTJhz70oUyaNCndu3ev+70effTR2nFLTzs+5phjstdeeyVJ5s6dm9WrV2911qxZs2rHI0aMaHa+f//+2X///ZMkzz//fF577bWtzpo/f35WrVqVJBk6dGhdnz4NAAAAAAAAAAAAAPXQbiLmjRs35sorr8z999+f5J2weNKkSc2ealwPjz32WGbPnp3knacdDx8+vNmazp07Z+TIkUmSVatWZfr06S3OqlarueOOO2qvTz755GZrKpVKRo8eXVt/++23b3Vvm59raRYAAAAAAAAAAAAAtLV2ETFXq9WMGzcu9913X5LkwAMPzG233Zb99tvvXc257777MmfOnFSr1a2umTdvXi6++OLamlNOOSW9e/duce2FF16YSqWSJLnhhhvy7LPPNltz00035YknnkiSHHHEERk1alSLs84999zsvffeSZJJkybl4YcfbrZm+vTpeeCBB5IkvXv3zhlnnLHVrwMAAAAAAAAAAAAA2kqHtt5APUyYMCFTp05Nkuy555750pe+lKeeeipPPfVUq9cde+yxtTA4SZ5++ulMnjw5vXv3zvDhwzNgwID06NEjDQ0NWbx4cWbPnr1F5Ny/f/9cccUVW50/aNCgnH/++bnllluycuXKjB07NmeccUaGDBmSpqamPPjgg7UnOnfq1Cnjx4/f6qxevXrl8ssvz9VXX53169fnggsuyJgxY3L00Udnw4YNmTlzZmbMmJEk6dChQ6655po0NjZu3zcQAAAAAAAAAAAAAApqFxHz448/Xjtet25dqzHw5h566KH069ev2fuvvvpqLYremhNPPDHjx4/PPvvs0+q6Sy+9NGvXrs3kyZPT1NSUyZMnN1vTs2fPXH/99Rk4cGCrs8aOHZumpqZMmDAh69aty7Rp0zJt2rQt1nTu3Dnjx4/Pcccd1+osAAAAAAAAAAAAAGgr7SJirpfzzz8/hx9+eP70pz9lwYIFWbZsWV5//fWsXbs2Xbp0Sb9+/XLkkUfmlFNOyeDBg7drZqVSyZVXXpmTTjop99xzT+bOnZslS5aksbExBxxwQI4//viMHTs2PXr02K555513XkaMGJG77747c+bMyZIlS1KpVNK3b9+MHDkyY8eOTd++fXfk2wAAAAAAAAAAAAAAO1W7iJhvv/32uszp1atXxowZkzFjxtRl3uaOPPLIHHnkkXWZNWDAgIwbN64uswAAAAAAAAAAAACgtIa23gAAAAAAAAAAAAAA8P4iYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFiZgBAAAAAAAAAAAAgKJEzAAAAAAAAAAAAABAUSJmAAAAAAAAAAAAAKAoETMAAAAAAAAAAAAAUJSIGQAAAAAAAAAAAAAoSsQMAAAAAAAAAAAAABQlYgYAAAAAAAAAAAAAihIxAwAAAAAAAAAAAABFdaj3wLlz59aOP/zhD2evvfaq9y0AAAAAAAAAAAAAgN1Y3SPmc845J5VKJUny0EMPpU+fPi2uW7x4cT7/+c8nSSqVSv7rv/6r3lsBAAAAAAAAAAAAAHZBdY+Yk6RardZC5q1Zv359XnvttSTZ5loAAAAAAAAAAAAAoP1o2BlDtydKXr9+/c64NQAAAAAAAAAAAACwi9spEXO1Wk3Sesz86KOP7oxbAwAAAAAAAAAAAAC7uA47OuC2227L5MmTWzw3duzY7LHHHs3eX7NmTZYvX55KpZJqtZqOHTvu6DYAAAAAAAAAAAAAgN3EDkfMK1euzCuvvNLs/Wq1mtdee22b11cqlRx88ME7ug0AAAAAAAAAAAAAYDexwxHzJpVKJck78fL/fW9bPvOZz9RrGwAAAAAAAAAAAADALq5uEfPm8XJr721x8w4dcsYZZ+QrX/lKvbYBAAAAAAAAAAAAAOzidjhiPuGEE9K3b98k70TLV155Ze0JzJdddlm6d+/e/KYdOqRHjx4ZPHhwunXrtqNbAAAAAAAAAAAAAAB2IzscMR922GE57LDDaq+vvPLKVKvVVCqVjB49On369NnRWwAAAAAAAAAAAAAA7cgOR8z/1w9/+MPacUtPYQYAAAAAAAAAAAAA3t/qHjGfeuqp9R4JAAAAAAAAAAAAALQjdY+YN/fqq69m4cKFefPNN7Nhw4ZW155yyik7cysAAAAAAAAAAAAAwC5ip0TMTz31VL7//e/nySef3O5rRMwAAAAAAAAAAAAA8P5Q94j5mWeeyTnnnJM1a9akWq1u1zWVSqXe2wAAAAAAAAAAAAAAdlF1j5h/8pOfZPXq1alUKtsVJ29v6AwAAAAAAAAAAAAAtA91j5jnz59fi5c3BcrdunVLx44d09DQUO/bAQAAAAAAAAAAAAC7mbpHzKtXr64dDx8+PD/+8Y/TrVu3et8GAAAAAAAAAAAAANhN1f3RyP369as9gfmSSy4RMAMAAAAAAAAAAAAAW6h7xHzSSSfVjteuXVvv8QAAAAAAAAAAAADAbq7uEfN5552XAw88MEnyb//2b2lqaqr3LQAAAAAAAAAAAACA3ViHeg+cMWNGPvOZz+Smm27KvHnz8vGPfzwnn3xyDjzwwHTr1m2r151yyin13goAAAAAAAAAAAAAsAuqe8T8ne98J5VKJUlSrVbzt7/9LXffffc2rxMxAwAAAAAAAAAAAMD7Q90j5s1tHjNvzzoAAAAAAAAAAAAAoP3bqRHzJq1FytsKnAEAAAAAAAAAAACA9qXuEXOfPn3qPRIAAAAAAAAAAAAAaEfqHjH/7ne/q/dIAAAAAAAAAAAAAKAdaWjrDQAAAAAAAAAAAAAA7y8iZgAAAAAAAAAAAACgqA71Hrho0aL3dF2fPn3qvBMAAAAAAAAAAAAAYFdU94j5E5/4RCqVyru6plKpZMGCBfXeCgAAAAAAAAAAAACwC6p7xJwk1Wp1Z4wFAAAAAAAAAAAAANqBnRIxv5snMQueAQAAAAAAAAAAAOD9pc2exPxuQmcAAAAAAAAAAAAAoP2oe8T80EMPbfXcG2+8kf/5n//JlClT8sc//jENDQ256qqrMmLEiHpvAwAAAAAAAAAAAADYRdU9Yu7bt2+r5wYPHpyTTz45V111VaZMmZIf/ehHGT58eL23AQAAAAAAAAAAAADsohra6sZf+MIXkiRvv/12br755rbaBgAAAAAAAAAAAABQWJtFzMuWLasdz549u622AQAAAAAAAAAAAAAU1qHeAxctWrTVcxs2bMjq1avz0ksv5brrrkulUkm1Ws3y5cvrvQ0AAAAAAAAAAAAAYBdV94j5E5/4RCqVyjbXVavV2rqePXvWexsAAAAAAAAAAAAAwC6q7hFz8k6gvC2bAuZKpZKPf/zjO2MbAAAAAAAAAAAAAMAuaKdEzNvzJObkndj5gx/8YC6++OKdsQ0AAAAAAAAAAAAAYBfUZk9i7tOnT0466aR89atfTdeuXXfGNgAAAAAAAAAAAACAXVDdI+aHHnqo9Rt26JAuXbqkc+fO9b41AAAAAAAAAAAAALAbqHvE3Ldv33qPBAAAAAAAAAAAAADakYa23gAAAAAAAAAAAAAA8P5S9ycxb27+/PmZOnVqHnvssSxdujRJst9+++Woo47KmWeemaFDh+7M2wMAAAAAAAAAAAAAu6CdEjGvW7cu3/ve9/LLX/4ySVKtVmvn/vKXv+Svf/1r7rvvvpxxxhm56qqr0qHDTm2pAQAAAAAAAAAAAIBdyE6ph8ePH59p06bVXlcqlS3Ob4qap02blkqlkmuuuWZnbAMAAAAAAAAAAAAA2AU11Hvgk08+mXvuuSeVSqX2q1qtbvFr8/enTp2aJ598st7bAAAAAAAAAAAAAAB2UXV/EvM999xTO65Wq/nABz6Qf/iHf0jfvn2TJK+88kr+8z//M8uWLdvimiFDhtR7KwAAAAAAAAAAAADALqjuEfNjjz2WSqWSJDn66KPzs5/9LHvttdcWa/75n/855557bubNm5dqtZp58+bVexsAAAAAAAAAAAAAwC6qod4DlyxZkmq1miS58MILmwXMSbLXXnvl61//+hbXAAAAAAAAAAAAAADvD3WPmNeuXVs73nfffbe6bvNz69evr/c2AAAAAAAAAAAAAIBdVN0j5u7du9eOf/vb32513YMPPlg7bi12BgAAAAAAAAAAAADalw71Hjho0KAsWbIk1Wo1N998c95+++2ceuqp6devX5Lkf//3f3PvvffmtttuS6VSSZIMHjy43tsAAAAAAAAAAAAAAHZRdY+YTzjhhPz+979PpVLJxo0bM2nSpEyaNKnZumq1miSpVCo58cQT670NAAAAAAAAAAAAAGAX1VDvgWPGjMnBBx+c5J1AuVqttvhr01OYDz744IwZM6be2wAAAAAAAAAAAAAAdlF1j5j33HPP3HjjjfnABz5Qi5Vb+lWtVvN3f/d3ufHGG9OhQ90fCA0AAAAAAAAAAAAA7KLqHjEnyaGHHpp77703p512Wvbcc89mT2Hec889c/rpp+eXv/xlDjnkkJ2xBQAAAAAAAAAAAABgF7XTHoH8gQ98ID/4wQ9y1VVX5amnnsrSpUuTJPvtt18OP/zwdOzYcWfdGgAAAAAAAAAAAADYhdUlYl6+fHnWrFmTJGlsbEzPnj1r5xobGzNs2LBm61esWNHiegAAAAAAAAAAAACgfWvY0QErV67MiSeemOOPPz7HH398HnjggW1eM2PGjNr6T37yk1m1atWObgMAAAAAAAAAAAAA2E3scMT8m9/8Jk1NTalWq+ndu3e+8IUvbPOasWPHpk+fPqlWq2lqaspvfvObHd0GAAAAAAAAAAAAALCb2OGIefbs2UmSSqWSU089NZVKZZvXVCqVnHbaabXXs2bN2tFtAAAAAAAAAAAAAAC7iR2OmJ999tna8bBhw7b7uqOOOqrFGQAAAAAAAAAAAABA+7bDEfPSpUtrx/vvv/92X9erV68kSbVa3WIGAAAAAAAAAAAAANC+7XDEvG7dutrx+vXrt/u6zde+m+sAAAAAAAAAAAAAgN3bDkfM3bp1qx0vXLhwu697/vnna8f77LPPjm4DAAAAAAAAAAAAANhN7HDE3KtXr9rxPffcs93XTZkyJUlSqVSy//777+g2AAAAAAAAAAAAAIDdxA5HzEcddVSSpFqt5tFHH82NN964zWv+/d//PX/84x9TqVS2mAEAAAAAAAAAAAAAtH87HDF/8pOfTPLOE5Wr1WpuuummXHDBBXnkkUeydu3a2rq1a9fm4Ycfzj/+4z9m4sSJtfWbzwAAAAAAAAAAAAAA2r8OOzpg2LBh+fCHP5wnn3yyFibPnj07s2fPzh577JFu3bolSd54441s2LAhyTtPba5UKqlUKvnwhz+cYcOG7eg2AAAAAAAAAAAAAIDdxA4/iTlJfvCDH6Rjx45J/t8TmavVatavX59ly5Zl2bJlWb9+fe39TWv23nvv/OAHP6jHFgAAAAAAAAAAAACA3URdIuZDDz00EydOTOfOnbd4yvLWflWr1XTp0iUTJ07MIYccUo8tAAAAAAAAAAAAAAC7ibpEzEkyfPjwTJkyJcOHD689cXlrv0aMGJEpU6bk2GOPrdftAQAAAAAAAAAAAIDdRId6Djv00ENz66235oUXXsjMmTPz3HPPZcWKFUmSHj165O///u9z3HHH5dBDD63nbQEAAAAAAAAAAACA3UhdI+ZNDj30UKEyAAAAAAAAAAAAANCihrbeAAAAAAAAAAAAAADw/iJiBgAAAAAAAAAAAACKEjEDAAAAAAAAAAAAAEWJmAEAAAAAAAAAAACAokTMAAAAAAAAAAAAAEBRImYAAAAAAAAAAAAAoCgRMwAAAAAAAAAAAABQlIgZAAAAAAAAAAAAAChKxAwAAAAAAAAAAAAAFCViBgAAAAAAAAAAAACKEjEDAAAAAAAAAAAAAEWJmAEAAAAAAAAAAACAokTMAAAAAAAAAAAAAEBRImYAAAAAAAAAAAAAoCgRMwAAAAAAAAAAAABQlIgZAAAAAAAAAAAAAChKxAwAAAAAAAAAAAAAFCViBgAAAAAAAAAAAACKEjEDAAAAAAAAAAAAAEWJmAEAAAAAAAAAAACAokTMAAAAAAAAAAAAAEBRImYAAAAAAAAAAAAAoCgRMwAAAAAAAAAAAABQlIgZAAAAAAAAAAAAAChKxAwAAAAAAAAAAAAAFCViBgAAAAAAAAAAAACKEjEDAAAAAAAAAAAAAEWJmAEAAAAAAAAAAACAokTMAAAAAAAAAAAAAEBRImYAAAAAAAAAAAAAoCgRMwAAAAAAAAAAAABQlIgZAAAAAAAAAAAAAChKxAwAAAAAAAAAAAAAFNWhrTdQLytXrsysWbPyxz/+MQsWLMhf/vKXrFq1Kp06dUrv3r0zdOjQnHbaaRkyZMh2z5w5c2amT5+eJ554IsuWLUuXLl1y4IEHZvTo0fnc5z6XTp06bfesxx9/PPfcc0/mzp2bpUuXprGxMf369csJJ5yQs846Kz169NjuWQsXLsyUKVMyZ86cLF68OA0NDenTp09GjhyZsWPHpm/fvts9CwAAAAAAAAAAAABKaxcR8y233JKf/OQnWbt2bbNzb775Zt58880899xzueuuu/LZz34211xzTfbee++tzlu7dm2+853v5Ne//vUW769YsSIrVqzI448/njvuuCMTJ07MYYcd1ureqtVqrr322tx2222pVqu191evXp2//e1vefrpp3PHHXfkxz/+cT760Y9u82v92c9+lgkTJmTdunVbvL9w4cIsXLgwd955Z8aPH59Pf/rT25wFAAAAAAAAAAAAAG2hXUTML7/8ci1gPuCAA/Kxj30shx12WLp3754333wzDz/8cB588MFs2LAhv/rVr7JixYrccsstaWhoaHHe5Zdfnvvvvz9J0q1bt3z+85/PgAED8vrrr+dXv/pVnnzyyfzlL3/J+eefn6lTp6Z3795b3dv111+fSZMmJUk6deqU008/PUOGDElTU1MefPDBzJkzJ8uWLcuFF16YO++8MwMHDtzqrLvuuis/+tGPkiR77rlnPvvZz+aYY47JunXrMnv27MyYMSNvvfVWvv3tb6dr16457rjj3su3EwAAAAAAAAAAAAB2qnYRMVcqlYwaNSrnnXdejjnmmGbnP//5z2fevHm54IIL0tTUlNmzZ+fee+/N6aef3mztb3/721rA3KdPn9xxxx3p06dP7fwXv/jF/Mu//EumT5+epUuX5oc//GF+8pOftLivBQsW5NZbb02SdO3aNb/4xS+2eHLzWWedlYkTJ+bGG29MU1NTvvvd72bq1KmpVCrNZi1ZsiTXXXddkqRDhw756U9/mo997GO182eeeWamT5+eK664IuvXr8+4ceMyY8aMNDY2bs+3EAAAAAAAAAAAAACKaflRxLuZyy67LP/xH//RYsC8ybBhw3LppZfWXt97770trrvxxhtrx1dfffUWAXOSNDQ05Kqrrqq9P2PGjCxcuLDFWTfddFOq1WqS5Fvf+tYWAfMmF110UYYMGZIkeeqpp/KHP/yhxVm33npr3n777STJl7/85S0C5k1OO+20jB49Okny6quvZtq0aS3OAgAAAAAAAAAAAIC21C4i5n333Xe71m0KfJO0GB6//PLLeeaZZ5IkBx10UEaOHNninI4dO+bMM8+svf7Nb37TbM2qVasyc+bMJEmXLl1y2mmntTirUqnk7LPPrr3e9BTozVWr1TzwwAO19eecc06Ls5Jsca6lWQAAAAAAAAAAAADQ1tpFxLy9OnfuXDtevXp1s/OzZ8+uHQ8fPrzVWSNGjKgdz5o1q9n5uXPnZu3atUmSo48+Onvvvfd7nvX8889n8eLFSZL+/fund+/eW501dOjQdOnSJUkyf/78rFq1qtWvAwAAAAAAAAAAAABKe19FzM8//3ztuE+fPs3Ob/505sGDB7c6a+DAgdljjz2SJC+88EKq1epW77WtWT169Ejfvn2TJCtWrMjy5cvf86yGhoYMGjQoSbJx48a8+OKLra4HAAAAAAAAAAAAgNLeVxHzlClTasejRo1qdv7ll1+uHW+KiremQ4cO6dWrV5Kkqamp9qTkTV566aXtnpVsGVVvfm29ZwEAAAAAAAAAAABAW+vQ1hsoZf78+Zk+fXqSpLGxMV/5ylearVm5cmXtuHv37tuc2a1btyxatChJ8uabb2b//fffoVktXVvvWa155plntnstwPvJ22+/ncTPSYBd0cCBA5O88xcL2wufNwC7Hp83APDu+T01AErweQNACT5vAHae98WTmJcuXZpvfvOb2bhxY5Lkkksu2SI43mTzP4hqbGzc5tzN17z11lu7zKyOHTtudRYAAAAAAAAAAAAAtLV2/yTmpqamXHjhhVm8eHGSZNSoUTn33HPbeFe7pk1PFQJgS5v+NqWfkwC7rk6dOrX1FurG5w3ArsvnDQBsP7+nBkAJPm8AKMHnDUDrHnvssfd8bbt+EvOaNWvyta99LU8++WSSZOjQoZkwYUIqlUqL6zf/g6g1a9Zs1/xNOnfuvMvMWr169VZnAQAAAAAAAAAAAEBba7cR89q1a3PRRRflkUceSZIMGTIkt9xyS6tPzOnatWvt+PXXX9/mPd54443a8T777FO3WZtfW+9ZAAAAAAAAAAAAANDW2mXEvG7dulxyySWZOXNmkmTQoEG59dZb06VLl1avO+igg2rHr7zySqtr169fn8WLFyd550nJvXr12uL8wQcfvN2zkmTRokUtXlvvWQAAAAAAAAAAAADQ1tpdxLx+/fpceuml+d3vfpckGTBgQH7+859n33333ea1AwYMqB0//fTTra595plnsmHDhiTJoYcemkqlssX5/v37b/esFStW1OLkHj16pGfPnu951saNG7NgwYIkSUNDQw455JBW1wMAAAAAAAAAAABAae0qYt6wYUMuu+yyzJgxI0nyoQ99KJMmTUr37t236/rhw4fXjmfPnt3q2lmzZtWOR4wY0ez8Mccck7322itJMnfu3Kxevfo9z+rfv3/233//JMnzzz+f1157bauz5s+fn1WrViVJhg4dus2nTwMAAAAAAAAAAABAae0mYt64cWOuvPLK3H///UmSgw8+OJMmTWr2VOPWHHTQQRk0aFCS5OWXX84f/vCHFtetWbMmU6dOrb0+6aSTmq3p3LlzRo4cmSRZtWpVpk+f3uKsarWaO+64o/b65JNPbramUqlk9OjRtfW33377Vr+Gzc+1NAsAAAAAAAAAAAAA2lq7iJir1WrGjRuX++67L0ly4IEH5rbbbst+++33rmd9/etfrx1/73vfy6JFi7Y4v3Hjxi3e/9SnPpUBAwa0OOvCCy9MpVJJktxwww159tlnm6256aab8sQTTyRJjjjiiIwaNarFWeeee2723nvvJMmkSZPy8MMPN1szffr0PPDAA0mS3r1754wzzmjtSwUAAAAAAAAAAACANtGhrTdQDxMmTKg9GXnPPffMl770pTz11FN56qmnWr3u2GOPrYXBm5xwwgk5+eSTc//99+eVV17JqaeemrPOOisDBgzIG2+8kfvuuy9PPvlkkmS//fbLFVdcsdX5gwYNyvnnn59bbrklK1euzNixY3PGGWdkyJAhaWpqyoMPPpjZs2cnSTp16pTx48dvdVavXr1y+eWX5+qrr8769etzwQUXZMyYMTn66KOzYcOGzJw5MzNmzEiSdOjQIddcc00aGxu3/c0DAAAAAAAAAAAAgMLaRcT8+OOP147XrVvXagy8uYceeij9+vVr9v51112XSqWSX//613njjTdy8803N1vzwQ9+MBMnTkzv3r1bvcell16atWvXZvLkyWlqasrkyZObrenZs2euv/76DBw4sNVZY8eOTVNTUyZMmJB169Zl2rRpmTZt2hZrOnfunPHjx+e4445rdRYAAAAAAAAAAAAAtJV2ETHX21577ZUbbrghp5xySn75y1/miSeeyPLly9O5c+ccdNBBGT16dD73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YUNmzZrVbM3mf6i1Zs2abc7cfE3nzlsGMu921urVq7c6CwAAAAAAAAAAAADamoj5PfrIRz5SO37xxRebne/atWvt+PXXX9/mvDfeeKPFa+s9CwAAAAAAAAAAAADamoj5PerWrVvteOXKlc3OH3zwwbXjV155ZZvzFi1a1OK19Z4FAAAAAAAAAAAAAG1NxPwebetpx/37968dP/30063OWrFiRS1O7tGjR3r27PmeZ23cuDELFixIkjQ0NOSQQw5pdT0AAAAAAAAAAAAAlCZifo8effTR2nFLTzs+5phjstdeeyVJ5s6dm9WrV2911qxZs2rHI0aMaHa+f//+2X///ZMkzz//fF577bWtzpo/f35WrVqVJBk6dGi6dOmyja8EAAAAAAAAAAAAAMoSMb8Hjz32WGbPnp3knacdDx8+vNmazp07Z+TIkUmSVatWZfr06S3OqlarueOOO2qvTz755GZrKpVKRo8eXVt/++23b3Vvm59raRYAAAAAAAAAAAAAtDUR82buu+++zJkzJ9Vqdatr5s2bl4svvri25pRTTknv3r1bXHvhhRemUqkkSW644YY8++yzzdbcdNNNeeKJJ5IkRxxxREaNGtXirHPPPTd77713kmTSpEl5+OGHm62ZPn16HnjggSRJ7969c8YZZ2z16wAAAAAAAAAAAACAttKhrTdQL3/9618zbdq0Ld577rnnasePPPJI1q9fv8X5T33qUxk0aFDt9dNPP53Jkyend+/eGT58eAYMGJAePXqkoaEhixcvzuzZs7eInPv3758rrrhiq3saNGhQzj///Nxyyy1ZuXJlxo4dmzPOOCNDhgxJU1NTHnzwwdoTnTt16pTx48dvdVavXr1y+eWX5+qrr8769etzwQUXZMyYMTn66KOzYcOGzJw5MzNmzEiSdOjQIddcc00aGxu387sHAAAAAAAAAAAAAOW0m4h50aJFufnmm7d6ft68eZk3b94W7x144IFbRMybvPrqq5k6dWqr9zvxxBMzfvz47LPPPq2uu/TSS7N27dpMnjw5TU1NmTx5crM1PXv2zPXXX5+BAwe2Omvs2LFpamrKhAkTsm7dukybNq1ZuN25c+eMHz8+xx13XKuzAAAAAAAAAAAAAKCttJuIuR7OP//8HH744fnTn/6UBQsWZNmyZXn99dezdu3adOnSJf369cuRRx6ZU045JYMH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AAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJmAEAAAAAAAAAAACAVCJmAAAAAAAAAAAAACCViBkAAAAAAAAAAAAASCViBgAAAAAAAAAAAABSiZgBAAAAAAAAAAAAgFQiZgAAAAAAAAAAAAAglYgZAAAAAAAAAAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJmAEAAAAAAAAAAACAVCJmAAAAAAAAAAAAACCViBkAAAAAAAAAAAAASCViBgAAAAAAAAAAAABSiZgBAAAAAAAAAAAAgFQiZgAAAAAAAAAAAAAglYgZAAAAAAAAAAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJmAEAAAAAAAAAAACAVCJmAAAAAAAAAAAAACCViBkAAAAAAAAAAAAASCViBgAAAAAAAAAAAABSiZgBAAAAAAAAAAAAgFQiZgAAAAAAAAAAAAAglYgZAAAAAAAAAAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJmAEAAAAAAAAAAACAVCJmAAAAAAAAAAAAACCViBkAAAAAAAAAAAAASCViBgAAAAAAAAAAAABSiZgBAAAAAAAAAAAAgFQiZgAAAAAAAAAAAAAglYgZAAAAAAAAAAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJmAEAAAAAAAAAAACAVCJmAAAAAAAAAAAAACCViBkAAAAAAAAAAAAASCViBgAAAAAAAAAAAABSiZgBAAAAAAAAAAAAgFQiZgAAAAAAAAAAAAAglYgZAAAAAAAAAAAAAEglYgYAAAAAAAAAAAAAUomYAQAAAAAAAAAAAIBUImYAAAAAAAAAAAAAIJWIGQAAAAAAAAAAAABIJWIGAAAAAAAAAAAAAFKJ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z9QAyOD9BoAM3m8A9h1XYt7Gtr+IKi8v3+n6bdd8/HHTqKWUe3Xo0GGHewEAAAAAAAAAAABAqbkSM0VbryoEQFNb/zal10nYfRUVFaUeodVUVlTufNEBpK29prWl77W29rUBaEu83wDArvMzNQAyeL8BIIP3G4CWPffcc3v8WFdi3sa2v4jasGHDTtdvu6aysmnUUsq91q9fv8O9AAAAAAAAAAAAAKDURMzb6NSpU/F4zZo1O11fX19fPD700ENbba9tH9vaewEAAAAAAAAAAABAqYmYt9G/f//icW1tbYtrN2/eHO+++25E/OFKyd27d29yfsCAAbu8V0TEypUrm31sa+8FAAAAAAAAAAAAAKUmYt5GVVVV8XjJkiUtrl26dGls2bIlIiIOP/zwKBQKTc4PHDhwl/eqq6srxsldu3aNbt267fFen376abzyyisREdGuXbv4sz/7sxbXAwAAAAAAAAAAAEA2EfM2RowYUTyeP39+i2vnzZtXPB45cuR254cOHRrt27ePiIiFCxfG+vXr93ivgQMHRo8ePSIiYvny5bFq1aod7vX888/HunXrIiLi2GOPjY4dO7b4PAAAAAAAAAAAAAAgm4h5G/37949BgwZFRMSKFStizpw5za7bsGFDzJgxo3j7tNNO225NZWVljBo1KiIi1q1bFzU1Nc3u1djYGNOnTy/ePv3007dbUygUYvTo0cX1d9555w6fw7bnmtsLAAAAAAAAAAAAAEpNxPxHvvvd7xaPf/SjH8XKlSubnP/000+b3H/qqadGVVVVs3tNmDAhCoVCRETceOON8eqrr263ZurUqbF48eKIiDj66KPjy1/+crN7XXDBBXHIIYdERMQdd9wRTz311HZrampq4vHHH4+IiJ49e8ZZZ53V0lMFAAAAAAAAAAAAgJIoK/UAreV///d/4/77729y32uvvVY8XrBgQWzevLnJ+VNPPbV45eWtTj755Dj99NPj0Ucfjdra2jjzzDNj3LhxUVVVFfX19fHggw/Giy++GBERn//852PSpEk7nGnQoEFx0UUXxa233hpr166N8ePHx1lnnRVDhgyJhoaGmDVrVsyfPz8iIioqKuLaa6/d4V7du3ePiRMnxjXXXBObN2+Ob3/72/H1r389jj/++NiyZUvMnTs3Zs6cGRERZWVl8S//8i9RXl6+C585AAAAAAAAAAAA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AAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQCoRMwAAAAAAAAAAAACQSsQMAAAAAAAAAAAAAKQSMQMAAAAAAAAAAAAAqUTMAAAAAAAAAAAAAEAqETMAAAAAAAAAAAAAkErEDAAAAAAAAAAAAACkEjEDAAAAAAAAAAAAAKlEzAAAAAAAAAAAAABAKhEzAAAAAAAAAAAAAJBKxAwAAAAAAAAAAAAApBIxAwAAAAAAAAAAAACpRMwAAAAAAAAAAAAAQKqyUg+wPzr//PPjmWee2aW1vXv3jt/+9rc7XTd37tyoqamJxYsXx/vvvx8dO3aMfv36xejRo2Ps2LFRUVGxy/MtWrQo7rvvvli4cGGsXr06ysvL47DDDouTTz45xo0bF127dt3lvQAAAAAAAAAAAAAgm4h5H9u4cWNcfvnl8cgjjzS5v66uLurq6mLRokUxffr0mDx5chx55JEt7tXY2Bg//vGP45e//GU0NjYW71+/fn18+OGHsWTJkpg+fXr89Kc/jeHDh++T5wMAAAAAAAAAAAAAe0vEvBNTp05t8XyHDh1aPD9x4sR49NFHIyKic+fOcc4550RVVVWsWbMmHnrooXjxxRfjf1joXwAAc5dJREFUrbfeiosuuihmzJgRPXv23OFeN9xwQ9xxxx0REVFRURHf+MY3YsiQIdHQ0BCzZs2KJ598Mt5///2YMGFC3H333VFdXb17TxYAAAAAAAAAAAAAEoiYd+Lkk0/e48fOnj27GDD36tUrpk+fHr169SqeP/fcc+PKK6+MmpqaWL16dVx33XVx8803N7vXK6+8ErfddltERHTq1CnuuuuuJlduHjduXEyePDmmTJkSDQ0N8cMf/jBmzJgRhUJhj+cHAAAAAAAAAAAAgH2hXakHaMumTJlSPL7mmmuaBMwREe3atYurr766eP/MmTNj2bJlze41derUaGxsjIiI733ve00C5q0uueSSGDJkSEREvPTSSzFnzpxWeR4AAAAAAAAAAAAA0JpEzPvIihUrYunSpRER0b9//xg1alSz6zp06BBnn3128fZjjz223Zp169bF3LlzIyKiY8eOMWbMmGb3KhQKcd555xVvb70KNAAAAAAAAAAAAADsT0TM+8j8+fOLxyNGjGhx7ciRI4vH8+bN2+78woULY+PGjRERcfzxx8chhxyyx3sBAAAAAAAAAAAAQKmVlXqA/d3FF18cr7zyStTX10dlZWX06NEj/vzP/zzOOuusqK6u3uHjli1bVjwePHhwix+juro6DjrooNiyZUu8/vrr0djYGIVCoXh++fLlu7xX165do3fv3lFbWxt1dXXxwQcfRLdu3Xb2NAEAAAAAAAAAAAAgjSsx78ScOXNi9erVsWnTpqivr49XX3017rrrrjjjjDNi0qRJsX79+mYft2LFiuJx7969W/wYZWVl0b1794iIaGhoiHfffbfJ+TfffHOX94qI6NWrV7OPBQAAAAAAAAAAAID9gSsx70Dnzp1jxIgRcdRRR8Wf/umfRmNjY9TW1sZ///d/x6JFiyIioqamJt5555247bbboqys6ady7dq1xeMuXbrs0sdbuXJlRER89NFH0aNHj73aq7nH7szSpUt3eS3sD7ZeDf3jho9LPEnrqPy/f/qzuP/55JNPIsLXBnbH1tfohoaGEk/Serzf7J/a4vdaW/naQIa2+BoQ4XVgf9QWv9d8nwGwr/mZGgAZvN8AkMH7DcC+I2Juxve///046qij4uCDD97u3N/+7d/GE088ET/4wQ/ik08+iaeeeipuvfXW+Lu/+7sm67b9pVZ5eflOP+a2az7+uGkg05p7AQAAAAAAAAAAAECpiZibccwxx7R4/q/+6q/i2muvjX/8x3+MiIif//znceGFF0b79u0zxttntl5VCA40lRWVO190APFncf+z9W9T+trA7quoqCj1CK3G+83+rS19r7W1rw1kaEuvARFeB/Znbel7zfcZAPuan6kBkMH7DQAZvN8AtOy5557b48e2a8U5PlO++tWvxoABAyIiYu3atdt9Ebb9pdaGDRt2ut+2ayormwYyrbkXAAAAAAAAAAAAAJSaiHkvDB06tHj8xhtvNDnXqVOn4vGaNWt2uld9fX3x+NBDD221vbZ9LAAAAAAAAAAAAADsD0TMe6FLly7F47Vr1zY5179//+JxbW1ti/ts3rw53n333Yj4w1WXu3fv3uT81is+78peERErV65s9rEAAAAAAAAAAAAAsD8QMe+Fba+K/MdXPK6qqioeL1mypMV9li5dGlu2bImIiMMPPzwKhUKT8wMHDtzlverq6oqhc9euXaNbt24trgcAAAAAAAAAAACAbCLmvbBw4cLi8R9f8XjEiBHF4/nz57e4z7x584rHI0eO3O780KFDo3379sWPuX79+j3eCwAAAAAAAAAAAABKTcS8hx5++OF44403IiKisrIyjjvuuCbn+/fvH4MGDYqIiBUrVsScOXOa3WfDhg0xY8aM4u3TTjttuzWVlZUxatSoiIhYt25d1NTUNLtXY2NjTJ8+vXj79NNP341nBAAAAAAAAAAAAAA5RMx/ZNq0abF48eIW18yePTv++Z//uXj7ggsuiPLy8u3Wffe73y0e/+hHP4qVK1c2Of/pp582uf/UU0+NqqqqZj/mhAkTolAoRETEjTfeGK+++up2a6ZOnVqc/eijj44vf/nLLT4PAAAAAAAAAAAAACiFslIPsL9ZsGBB/Ou//msMGDAghg8fHl/4wheiS5cu0djYGLW1tfHb3/42Fi1aVFw/bNiwuPjii5vd6+STT47TTz89Hn300aitrY0zzzwzxo0bF1VVVVFfXx8PPvhgvPjiixER8fnPfz4mTZq0w7kGDRoUF110Udx6662xdu3aGD9+fJx11lkxZMiQaGhoiFmzZsX8+fMjIqKioiKuvfbaVvysAAAAAAAAAAAAAEDrETHvwJtvvhlvvvnmDs8XCoUYO3ZsTJo0Kdq3b7/Ddddff30UCoV45JFHor6+Pm655Zbt1vTt2zcmT54cPXv2bHGmyy67LDZu3BjTpk2L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+7d/i8bGxpg4cWL84he/iM997nPFNRs2bIiJEydGQ0NDRESce+650aVLl1KNDCRp6RcgFRUV8Sd/8icxaNCgOOWUU+KUU06Jgw8+OHE6TjnllPj9738fERGHHXZYzJ49OwqFQomnKr3Zs2fH0qVLIyLiW9/6Vhx66KElngj4LHvhhRfioYceihdeeCFqa2tj3bp1UVZWFp07d46+ffvGEUccEV/84hfjS1/6UvEvFm7r7bffjl//+tcRETF06NAYNmxY9lMAaFWvvfZazJw5M373u9/FypUrY82aNdGhQ4fo2rVrHHXUUTFy5MgYPXp0dOjQodSjfmatXbs2/vM//zPmzJkTr732WtTX18emTZuioqIievToEQMGDIijjjoqhg0bFkcffXS0a+c6BgB764orrogHHnggIiIKhUI88cQT0adPnxJPBQC77sQTT4za2tqIiJg7d2507959h2u3bNkSw4YNi7Vr10ZExJgxY+K6665rcf877rijuOab3/xmXHnlla00+f7r6quvjnvvvbfUYwC7YE/+UuGRRx4Zv/nNb/bBNH/gdwvsqsmTJ8eUKVOaPXfwwQdHZWVl9OnTJ774xS/GmDFjYtCgQckT0pynn346nnnmmYiIOPPMM+Owww4r8USw/xIxH0DGjx8fs2bNimeffTaWLFkSX//61+Occ86Jfv36xapVq+L++++P119/PSIivvCFL8SECRNKPDFQag0NDfHWW2/FW2+9FY8//nhUVVXFzTffHAMGDCj1aJ8JCxcuLAbMEX/4D9Gnn346/uIv/qKEU+0fZs+eXfyP8jPPPFPEDJTE2rVr48orr4yZM2dud27z5s2xatWqWLVqVTzzzDNx5513RqFQiOeffz4qKiqarK2trS3+8OiSSy7xg0bggPXee+/F9ddfH4888kg0NjY2Obdx48b46KOPYsWKFfHwww/HTTfdFJdddll87WtfK9G0n11PPPFEXHXVVVFXV7fduY8++ig++uijWLZsWfH97aKLLoof/OAH2WMCtCkNDQ3x2GOPFW83NjbGr3/967j00ktLOBUA7J7jjz++GDE/88wz8dWvfnWHa5cuXVoMmLeu35mFCxcWjz8LPx9bsmRJMWDu0qVLnH/++TFgwIBo3759REQMGTKklOMBBwC/W6A1bNq0Kerr66O+vj5eeumluPPOO+Occ86Jq6++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tX+RSFSk8qlSUueGiIiIiIiIiIiISi9mYiYiIiIiIiIiIiKiDyokJATJyckK740aNQr9+/eHhYUFRCIRvL298b///U+n/To5OcHPzw8AkJubi9mzZ2P37t1o06aNwnZVq1bF48ePFb57/Pjxhe6/WrVqOpXnffXt2xd//vknMjIyAADe3t4wMDBQ2MbV1VWrfcXHx6NRo0ZK78mrWrWqwvLHfG6IiIiIiIiIiIio9GImZiIiIiIiIiIiIiIqFuXKKebRUJedt2AAs6mpKRYuXIhWrVqhVq1asLGxwf3793X+/r/++gstW7ZU+P6pU6ciMjJSYTt7e3uF11evXoWZmRlsbGxU/leuXDk8efIE5cuX17lM76NChQoYOHCg8DotLQ379u0TXletWhWdO3fWal8eHh4Kr8ViMXx8fBTea968ubD8sZ8bIiIiIiIiIiIiKr0YxExERERERERERERExcLCwkLh9YMHD+Dr64unT58iLi5OCF42NzdX2C4jIwNubm6IiopCaGgofvnlF5w7d07n769QoQK2bduG2rVrC++lp6dj4sSJSEhIEN4bPHiwQmbj2NhYjBw5Ep6ennj48CGePHmCmzdv4t9//8WECRPg5OSkFPhb3L755huIRCLhtVgsFpb79u2rFDCuztmzZ7Fs2TLcvXsXgYGB+O677/D8+XOFbfr27Sssl4ZzQ0RERERERERERKWTdq2aREREREREREREREQ6atWqlcJrsViM6dOnC6/btGmDQ4cOoU2bNqhcuTLS09OFdRs3bsTGjRuF11WrVkVKSorOZbCwsMA///yD4cOHIy0tDQDw/PlzTJgwAQcPHoSFhQWsra0xe/ZsrF27Vvjco0eP8OOPP+r8fcXF1tYW7du3x40bN5TWyWdpLoyRkRH279+P/fv3q1zfunVr9OzZU3hdGs4NERERERERERERlU7MxExERERERERERERExaJx48bo0qVLodsZGxtj8eLFKFNGdZO1nZ2dQvCzrurWrYstW7agfPnywnvR0dGYMmUKsrKyAACTJ0/GggULFLIOa2JlZfXe5XlfI0eOVHqvcePGaNy4sdb7WLlyJUxNTVWus7a2xvr165X+DqXh3BAREREREREREVHpwyBmIiIiIiIiIiIiIio2mzZtwtSpU2Fra6sQRFyQi4sL9u7di86dO6NSpUowMjJCgwYNMGfOHOzduxdGRkZFKkebNm2wdu1ahQDdu3fvYubMmRCLxQCASZMm4ezZs5g6dSpat24NMzMzlCtXDhUqVEDt2rXh5OSEX375BefPn8fcuXOLVJ730aNHD6UAYVdXV5320bJlS3h4eGDIkCGwsrKCgYEBrK2tMW7cOJw4cQI1a9ZU+bmP/dwQERERERERERFR6SOSSCSSD10IIiIiIiIiIiIiIiIq3IgRIxASEgIAKFeuHC5fvoyqVauq3DYuLg5OTk4K7/n5+cHGxqbYy0lERERERERERERUGGZiJiIiIiIiIiIiIiIqBc6dOycEMAPSzMzqApiJiIiIiIiIiIiIPnblPnQBiIiIiIiIiIiIiIhItXPnzmHNmjXIzMxEamqq8L5IJMKUKVM+YMmIiIiIiIiIiIiIioZBzEREREREREREREREH6nMzEw8ffpU6f0pU6agefPmH6BERERERERERERERPrBIGYiIiIiIiIiIiIiolLAxMQEtra2GDduHJydnT90cYiIiIiIiIiIiIiKRCSRSCQfuhBERERERERERERERERERERERERERET0+SjzoQtAREREREREREREREREREREREREREREnxcGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlSgGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlSgGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlSgGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlSgGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlSgGMRMREREREREREREREREREREREREREVGJYhAzERERERERERERERERERERERERERERlaj/B/vevxUYEClqAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1440x1080 with 1 Axes>"
      ]
     },
     "metadata": {
      "image/png": {
       "height": 1072,
       "width": 1432
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax=plt.subplots(figsize=(20,15))\n",
    "sns.histplot(x='Intake Type', hue='Outcome Type', data=Dog_Outcome, multiple='dodge', ax=ax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a5437f95",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:57.595794Z",
     "iopub.status.busy": "2024-10-11T19:10:57.589838Z",
     "iopub.status.idle": "2024-10-11T19:10:57.628574Z",
     "shell.execute_reply": "2024-10-11T19:10:57.627774Z",
     "shell.execute_reply.started": "2022-12-16T15:25:37.030309Z"
    },
    "papermill": {
     "duration": 0.152333,
     "end_time": "2024-10-11T19:10:57.628771",
     "exception": false,
     "start_time": "2024-10-11T19:10:57.476438",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Create a locations file\n",
    "Locations = Dog_Outcome['Found Location']\n",
    "Locations = Locations.replace(to_replace = ' in ', value=' ', regex=True)\n",
    "Locations = Locations.to_frame()\n",
    "Locations = Locations.drop_duplicates(keep='first')\n",
    "#Locations_File = Locations.to_csv('Austin Found Locations.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "17224f97",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-10-11T19:10:57.838434Z",
     "iopub.status.busy": "2024-10-11T19:10:57.837489Z",
     "iopub.status.idle": "2024-10-11T19:10:58.157839Z",
     "shell.execute_reply": "2024-10-11T19:10:58.156963Z",
     "shell.execute_reply.started": "2022-12-16T15:25:38.030269Z"
    },
    "papermill": {
     "duration": 0.428807,
     "end_time": "2024-10-11T19:10:58.158241",
     "exception": true,
     "start_time": "2024-10-11T19:10:57.729434",
     "status": "failed"
    },
    "tags": []
   },
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '/kaggle/input/austin-found-locations/Austin Found Locations (1).csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_19/3223352038.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m### Upload that new file\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mLocations\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/kaggle/input/austin-found-locations/Austin Found Locations (1).csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/util/_decorators.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    309\u001b[0m                     \u001b[0mstacklevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstacklevel\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    310\u001b[0m                 )\n\u001b[0;32m--> 311\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    312\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    313\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[1;32m    584\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    585\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 586\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    587\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    588\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    480\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    481\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 482\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    483\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    484\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m    809\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"has_index_names\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"has_index_names\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    810\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 811\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    812\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    813\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, engine)\u001b[0m\n\u001b[1;32m   1038\u001b[0m             )\n\u001b[1;32m   1039\u001b[0m         \u001b[0;31m# error: Too many arguments for \"ParserBase\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1040\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mmapping\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1041\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1042\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_failover_to_python\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/c_parser_wrapper.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, src, **kwds)\u001b[0m\n\u001b[1;32m     49\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     50\u001b[0m         \u001b[0;31m# open handles\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 51\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_open_handles\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     52\u001b[0m         \u001b[0;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhandles\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     53\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/parsers/base_parser.py\u001b[0m in \u001b[0;36m_open_handles\u001b[0;34m(self, src, kwds)\u001b[0m\n\u001b[1;32m    227\u001b[0m             \u001b[0mmemory_map\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"memory_map\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    228\u001b[0m             \u001b[0mstorage_options\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"storage_options\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 229\u001b[0;31m             \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"encoding_errors\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"strict\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    230\u001b[0m         )\n\u001b[1;32m    231\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.7/site-packages/pandas/io/common.py\u001b[0m in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    705\u001b[0m                 \u001b[0mencoding\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencoding\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    706\u001b[0m                 \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 707\u001b[0;31m                 \u001b[0mnewline\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    708\u001b[0m             )\n\u001b[1;32m    709\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '/kaggle/input/austin-found-locations/Austin Found Locations (1).csv'"
     ]
    }
   ],
   "source": [
    "### Upload that new file\n",
    "Locations = pd.read_csv('/kaggle/input/austin-found-locations/Austin Found Locations (1).csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4f24bfd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:40.08269Z",
     "iopub.status.busy": "2022-12-16T15:25:40.081791Z",
     "iopub.status.idle": "2022-12-16T15:25:40.086292Z",
     "shell.execute_reply": "2022-12-16T15:25:40.085428Z",
     "shell.execute_reply.started": "2022-12-16T15:25:40.082652Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Use Nominatim via geopy.geocoders\n",
    "# CAVEAT: Bulk geocoding did not work out, so I used geocodio.io to upload my excel files in batches of 500 to create a small sample size\n",
    "#from geopy.geocoders import Nominatim\n",
    "#geolocator = Nominatim(user_agent=\"my_application\")\n",
    "#location = geolocator.geocode('6111 Softwood Dr Austin TX')\n",
    "#print(location.latitude, location.longitude)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1e24d8f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:41.212613Z",
     "iopub.status.busy": "2022-12-16T15:25:41.21228Z",
     "iopub.status.idle": "2022-12-16T15:25:41.247878Z",
     "shell.execute_reply": "2022-12-16T15:25:41.246992Z",
     "shell.execute_reply.started": "2022-12-16T15:25:41.212574Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Loaded up the transformed files with lat, lon included\n",
    "Locs_500 = pd.read_csv('/kaggle/input/austin-found-locations/500_Austin_Found (1).csv')\n",
    "Locs_501 = pd.read_csv('/kaggle/input/austin-found-locations/Austin_501t1000 (1).csv')\n",
    "Locs_1001 = pd.read_csv('/kaggle/input/austin-found-locations/Austin_1001t1500 (1).csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "098856f2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:42.924752Z",
     "iopub.status.busy": "2022-12-16T15:25:42.924078Z",
     "iopub.status.idle": "2022-12-16T15:25:42.933383Z",
     "shell.execute_reply": "2022-12-16T15:25:42.932786Z",
     "shell.execute_reply.started": "2022-12-16T15:25:42.924694Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Change it so that given_address is Found Location and drop all na values\n",
    "i = Locs_500.fillna(value=0)\n",
    "i = i.rename(columns={\"given_address\": \"Found Location\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22155154",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:43.917663Z",
     "iopub.status.busy": "2022-12-16T15:25:43.917126Z",
     "iopub.status.idle": "2022-12-16T15:25:43.929271Z",
     "shell.execute_reply": "2022-12-16T15:25:43.928635Z",
     "shell.execute_reply.started": "2022-12-16T15:25:43.91761Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "L501 = Locs_501.fillna(value=0)\n",
    "L501 = Locs_501.rename(columns={\"given_address\": \"Found Location\"})\n",
    "L1001 = Locs_1001.fillna(value=0)\n",
    "L1001 = Locs_1001.rename(columns={\"given_address\": \"Found Location\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e76a9d5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:45.26087Z",
     "iopub.status.busy": "2022-12-16T15:25:45.260126Z",
     "iopub.status.idle": "2022-12-16T15:25:45.283661Z",
     "shell.execute_reply": "2022-12-16T15:25:45.282709Z",
     "shell.execute_reply.started": "2022-12-16T15:25:45.260816Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import folium\n",
    "m = folium.Map(location = [30.27,-97.74])\n",
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d87c2abb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:53.97605Z",
     "iopub.status.busy": "2022-12-16T15:25:53.975722Z",
     "iopub.status.idle": "2022-12-16T15:25:53.983606Z",
     "shell.execute_reply": "2022-12-16T15:25:53.982939Z",
     "shell.execute_reply.started": "2022-12-16T15:25:53.976017Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## turn lat,lon into coordinates that folium can work with\n",
    "coords = i[['lat', 'lon']]\n",
    "coords_list = coords.values.tolist()\n",
    "len(coords_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac3b16d8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:25:54.858418Z",
     "iopub.status.busy": "2022-12-16T15:25:54.857822Z",
     "iopub.status.idle": "2022-12-16T15:25:54.913005Z",
     "shell.execute_reply": "2022-12-16T15:25:54.912306Z",
     "shell.execute_reply.started": "2022-12-16T15:25:54.858365Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "for point in range(0, len(coords_list)):\n",
    "    folium.Marker(location=coords_list[point], popup=i['suburb'][point],).add_to(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46de5a09",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:26:09.775832Z",
     "iopub.status.busy": "2022-12-16T15:26:09.775278Z",
     "iopub.status.idle": "2022-12-16T15:26:10.536168Z",
     "shell.execute_reply": "2022-12-16T15:26:10.535352Z",
     "shell.execute_reply.started": "2022-12-16T15:26:09.775795Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0faf736a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:26:25.094712Z",
     "iopub.status.busy": "2022-12-16T15:26:25.09442Z",
     "iopub.status.idle": "2022-12-16T15:26:25.10523Z",
     "shell.execute_reply": "2022-12-16T15:26:25.104455Z",
     "shell.execute_reply.started": "2022-12-16T15:26:25.094682Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Append the 1500 found locations\n",
    "d = i.append(L501)\n",
    "e = d.append(L1001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ead8984",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:26:26.019711Z",
     "iopub.status.busy": "2022-12-16T15:26:26.019358Z",
     "iopub.status.idle": "2022-12-16T15:26:26.060382Z",
     "shell.execute_reply": "2022-12-16T15:26:26.059458Z",
     "shell.execute_reply.started": "2022-12-16T15:26:26.019672Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Merge with Dogs_Outcome Data Frame. Merge as many geocoded addresses as possible\n",
    "combo= e.merge(Dog_Outcome, how='left', on='Found Location')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a513027c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:26:26.953857Z",
     "iopub.status.busy": "2022-12-16T15:26:26.953527Z",
     "iopub.status.idle": "2022-12-16T15:26:26.968454Z",
     "shell.execute_reply": "2022-12-16T15:26:26.96748Z",
     "shell.execute_reply.started": "2022-12-16T15:26:26.95382Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## After merge, drop unneeded columns\n",
    "combo.columns\n",
    "combo = combo.drop(columns={'confidence_city_level', 'confidence_street_level', 'attribution',\n",
    "       'attribution_license', 'attribution_url'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee77fc12",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-16T15:26:28.13982Z",
     "iopub.status.busy": "2022-12-16T15:26:28.139281Z",
     "iopub.status.idle": "2022-12-16T15:26:28.183773Z",
     "shell.execute_reply": "2022-12-16T15:26:28.182882Z",
     "shell.execute_reply.started": "2022-12-16T15:26:28.139767Z"
    },
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "combo"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0ca5c69",
   "metadata": {
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "source": [
    "## Now you can plot clusters to find out where most dogs are taken in by animal control.\n",
    "\n",
    "Thank you for following along, as you can see, I am all over the place, but I have good intentions with the erratic thoughts. Feedback is appreciated. I did not fully complete this project, i.e. I forgot to do a comparison with the Washington Dataset and I left Intake Dogs dataset high and dry, but I wanted to get this out there or else it would never see the light of day to benefit from public feedback."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e31ba48c",
   "metadata": {
    "papermill": {
     "duration": null,
     "end_time": null,
     "exception": null,
     "start_time": null,
     "status": "pending"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 1899123,
     "sourceId": 3111430,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 1899251,
     "sourceId": 3111654,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30157,
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 86.211275,
   "end_time": "2024-10-11T19:10:59.576936",
   "environment_variables": {},
   "exception": true,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-10-11T19:09:33.365661",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
