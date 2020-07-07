# calculadoranutricional

1 - Introduction

This script calculates the total energy expendure for hospitalized patients, body mass index and classify the BMI by gender and age. The metabolic rate is calculated using Harris and Benedict equation.

2 - Techinical talking points

This script may be useful to assess the patient quickly, specially in crowded hospitals with low budget.

3 - Technologies and languages

The repository only uses Python 3.8.

4 - Setup and use

The only thing you'll need is to download the source code and run it on your favorite Python IDE.

Once the script is runing, it'll ask you for a few inputs:

    • Gender - Just enter type the gender of the patient. Use M to MALE or F to FEMALE

    • Weight - Type the weight of the patient in Kilograms, and separete the decimals with comma

    • Height - Type the height of the patient in meters, and separete the decimals with comma

    • Age - Type the age of the patient in years, without the months

    • Active factor - Type the active factor according to the condition of the patient

    • Injury factor - Type the injury factor according to the condition of the patient

    • Thermal factor - Type the thermal factor according to the condition of the patient


If you use injury factor, except in heart failure, use active factor as 1. And, if the patient doesn't have any complications, use injury factor as 1.

5 - Contributions, issues and forking

The objective is to create a useful tool to any hospital. Any contribuitions are welcome, fell free to leave a suggestion

6 - About me

Hi there! I'm an undergraduated nutrition student who fell in love with programing in a quarentine. So I created this repository to train coding and to apply the knowledge of nutrition on a real scenario. It may not be perfect (as well as my English), but I'm trying my best to learn a new field of knowledge.

8 - Show your support

I don't have in mind to be the best programmer in the world, but I'm here to learn from my mistakes. That said, if you may, please leave a star and point out some improvements I can make on the code. Or even send me a message with some tips to make my learning process easier, all help is welcome. Thanks


9 - Useful links and tools
Factors

• Active factor

    • Bedridden - 1.2
    • Bedridden mobile - 1.25
    • Wandering - 1.3


• Injury factor

    • Cancer - 1.1 to 1.45
    • Elective surgery - 1.0 to 1.1
    • Severe malnutrition - 1.5
    • Multiple fractures - 1.2 to 1.35
    • Severe infection - 1.3 to 1.35
    • Heart failure - 1.3 to 1.5 (without active factor)
    • Liver failure - 1.3 to 1.55
    • Acute renal failure - 1.3
    • Weight maintence - 1.2 to 1.5
    • Elective operation - 1.75
    • Uncomplicated patient - 1.0
    • Pancreatitis - 1.3 to 1.8
    • Minor surgery - 1.2
    • Small tissue trauma - 1.14 to 1.37
    • Skin burn (up to 20%) - 1.0 to 1.5
    • Skin burn (20 to 40%) - 1.5 to 1.85
    • Skin burn (40 to 100%) - 1.85 to 2.05
    • Extensive skin burn - 2.7
    • Polytraumatized - 1.9
    • Peritonitis - 1.2 to 1.5
    • Postoperative cardiac surgery - 1.2 to 1.5
    • Postoperative genral surgery - 1.0 to
    • Septicemia - 1.6
    • Liver transplant - 1.2 to 1.5
    • Bone marrow transplant - 1.2 to 1.3
    • Skeletal trauma - 1.35
