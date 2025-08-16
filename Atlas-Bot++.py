import discord
from discord.ext import commands

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

# Enable necessary intents
bot.intents.message_content = True
bot.intents.guilds = True
bot.intents.members = True


a = [
    # Countries
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan",
    # Cities
    "Amsterdam", "Athens", "Atlanta", "Adelaide", "Auckland", "Aberdeen",
    "Albuquerque", "Alexandria", "Anchorage", "Ann Arbor", "Annapolis",
    "Austin", "Albany", "Akron", "Amarillo", "Asheville", "Aspen",
    "Atlantic City", "Augusta", "Aurora", "Abuja", "Accra", "Addis Ababa",
    "Algiers", "Almaty", "Amman", "Ankara", "Antananarivo", "Apia",
    "Ashgabat", "Asmara", "Astana", "Asuncion", "Allentown", "Abilene",
    "Anaheim", "Arlington", "Arvada", "Ashland", "Ames", "Appleton",
    "Anderson", "Alameda", "Antioch", "Apple Valley", "Arcadia", "Ashburn",
    "Auburn", "Aventura", "Avondale", "Aarhus", "Agra", "Ahmedabad",
    "Aleppo", "Almere", "Antalya", "Antwerp", "Arequipa", "Astrakhan",
    "Aswan", "Athenry", "Augsburg", "Avignon", "Ayacucho", "Azul",
    # States
    "Alabama", "Alaska", "Arizona", "Arkansas", "Acre", "Alagoas", "Amapa",
    "Amazonas", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Alberta",
    "Australian Capital Territory", "Aguascalientes",
    # Continents
    "Africa", "Antarctica", "Asia", "Australia",
]

b = [
    # Countries
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
    "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
    "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    # Cities
    "Barcelona", "Berlin", "Beijing", "Bangkok", "Buenos Aires", "Boston",
    "Baltimore", "Birmingham", "Buffalo", "Baton Rouge", "Bakersfield",
    "Bridgeport", "Boise", "Burlington", "Beaumont", "Billings", "Bismarck",
    "Bloomington", "Boulder", "Bristol", "Brighton", "Brisbane", "Brussels",
    "Bucharest", "Budapest", "Bangalore", "Bogota", "Brasilia", "Beirut",
    "Baghdad", "Baku", "Bamako", "Bangui", "Banjul", "Bissau",
    "Bloemfontein", "Brazzaville", "Bujumbura", "Bordeaux", "Bremen",
    "Brno", "Bursa", "Bern", "Basel", "Bradford", "Blackpool", "Bath",
    "Ballarat", "Bendigo", "Bathurst", "Bundaberg", "Brownsville",
    "Berkeley", "Beverly Hills", "Burbank", "Bellevue", "Bakersfield",
    # States
    "Bavaria", "Brandenburg", "Bremen", "Baden-Württemberg", "Bihar",
    "Bahia", "Baja California", "Baja California Sur", "British Columbia",
    "Balochistan", "Bengal", "Baden", "Basilicata", "Burgenland",
    # Continents
]
c = [
    # Countries
    "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czech Republic",
    # Cities
    "Cairo", "Chicago", "Charlotte", "Columbus", "Cleveland", "Cincinnati",
    "Colorado Springs", "Corpus Christi", "Chandler", "Chula Vista",
    "Chesapeake", "Cambridge", "Camden", "Carlsbad", "Carrollton", "Cary",
    "Cedar Rapids", "Centennial", "Charleston", "Chattanooga", "Cheyenne",
    "Clearwater", "Clovis", "College Station", "Columbia", "Concord",
    "Coral Springs", "Corona", "Costa Mesa", "Cranston", "Copenhagen",
    "Cologne", "Casablanca", "Chennai", "Chengdu", "Chongqing", "Caracas",
    "Cape Town", "Casablanca", "Calgary", "Canberra", "Christchurch",
    "Cardiff", "Cordoba", "Curitiba", "Cebu City", "Chandigarh",
    # States
    "California", "Colorado", "Connecticut", "Ceara", "Chihuahua", "Coahuila",
    "Colima", "Catalonia", "Castile and Leon", "Castile-La Mancha",
    "Canary Islands", "Cantabria", "Corsica", "Crete", "Cyprus", "Carinthia",
    "Central Java", "Central Kalimantan", "Central Sulawesi", "Chhattisgarh",
    "Chandigarh", "Chubut", "Cordoba", "Corrientes", "Cundinamarca",
    # Continents
]
d = [
    # Countries
    "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Democratic Republic of the Congo",
    # Cities
    "Dallas", "Denver", "Detroit", "Durham", "Dayton", "Daly City",
    "Danbury", "Davenport", "Davie", "Davis", "Daytona Beach", "Dearborn",
    "Decatur", "Delano", "Denton", "Des Moines", "Downey", "Duluth",
    "Dublin", "Damascus", "Dhaka", "Delhi", "Doha", "Dubai", "Durban",
    "Dortmund", "Dresden", "Dusseldorf", "Douala", "Dakar", "Dar es Salaam",
    "Darwin", "Dunedin", "Dundee", "Dijon", "Diyarbakir", "Dnipro",
    "Donetsk", "Drammen", "Debrecen", "Davao City", "Denpasar",
    # States
    "Delaware", "Dakota", "Durango", "Distrito Federal", "Drenthe",
    "Dalarnas", "Dalarna", "Damascus Governorate", "Dakahlia", "Damietta",
    "Dumfries and Galloway", "Derbyshire", "Devon", "Dorset", "Durham",
    "Diyala", "Dhi Qar", "Dahuk", "Dagestan", "Don", "Donetsk Oblast",
    # Continents
]
e = [
    # Countries
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
    "Estonia", "Eswatini", "Ethiopia",
    # Cities
    "El Paso", "Elizabeth", "Elk Grove", "Elgin", "Eugene", "Evansville",
    "Erie", "Escondido", "Euless", "Everett", "Edinburg", "Edmond",
    "El Cajon", "El Monte", "Elmhurst", "Elyria", "Encinitas", "Englewood",
    "Enterprise", "Euclid", "Evanston", "Exeter", "Edinburgh", "Exeter",
    "Essen", "Eindhoven", "Espoo", "Erfurt", "Erlangen", "Eskisehir",
    "Exeter", "Erbil", "Eskisehir", "Esbjerg", "Ecatepec", "Ensenada",
    "Essen", "Esslingen", "Ethekwini", "Evora", "Extrema",
    # States
    "Espirito Santo", "Estado de Mexico", "Extremadura", "East Java",
    "East Kalimantan", "East Nusa Tenggara", "East Timor", "Eastern Cape",
    "Eastern Province", "Eindhoven", "Emilia-Romagna", "England",
    "Eps", "Essex", "East Midlands", "East Anglia", "East Sussex",
    "East Yorkshire", "Edinburgh", "Erfurt", "Espoo", "Estonia",
    # Continents
    "Europe",
]
f = [
    # Countries
    "Fiji", "Finland", "France",
    # Cities
    "Fresno", "Fort Worth", "Fremont", "Fontana", "Fayetteville", "Fullerton",
    "Fort Lauderdale", "Fort Wayne", "Fort Collins", "Fall River",
    "Fargo", "Farmington", "Flint", "Florence", "Folsom", "Forest Park",
    "Fort Myers", "Fort Smith", "Franklin", "Frederick", "Fredericksburg",
    "Freeport", "Florence", "Frankfurt", "Freiburg", "Fukuoka", "Fortaleza",
    "Florence", "Ferrara", "Foggia", "Friuli", "Funchal", "Faro",
    "Famagusta", "Fes", "Freetown", "Florianopolis", "Feira de Santana",
    "Fortaleza", "Fukushima", "Fuzhou", "Faridabad", "Firozabad",
    # States
    "Florida", "Flanders", "Friesland", "Friuli-Venezia Giulia",
    "Free State", "Federal District", "Fujian", "Fukuoka", "Fukushima",
    "Fars", "Faryab", "Farah", "Flevoland", "Finnmark", "Funen",
    "Falmouth", "Fife", "Flintshire", "Fordshire",
    # Continents
]
g = [
    # Countries
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    # Cities
    "Garland", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids",
    "Green Bay", "Greensboro", "Gresham", "Garden Grove", "Gary",
    "Georgetown", "Glendale", "Gloucester", "Goodyear", "Grand Junction",
    "Gulfport", "Gastonia", "Gainesville", "Galveston", "Geneva",
    "Glasgow", "Gothenburg", "Genoa", "Granada", "Grenoble", "Gdansk",
    "Graz", "Ghent", "Geneva", "Guadalajara", "Guayaquil", "Guatemala City",
    "Gaborone", "Giza", "Gaza", "Guangzhou", "Guwahati", "Gwalior",
    "Goiania", "Guarulhos", "Gold Coast", "Geelong", "Gatineau",
    # States
    "Georgia", "Gujarat", "Goa", "Goias", "Galicia", "Gelderland",
    "Groningen", "Gauteng", "Gyeonggi", "Gangwon", "Guangdong", "Guangxi",
    "Guizhou", "Gansu", "Gilgit-Baltistan", "Ghazni", "Ghor",
    "Gloucestershire",
    "Greater Manchester", "Gwynedd", "Glamorgan",
    # Continents
]
h = [
    # Countries
    "Haiti", "Honduras", "Hungary",
    # Cities
    "Houston", "Henderson", "Hialeah", "Huntington Beach", "Huntsville",
    "Hampton", "Hartford", "Hayward", "Hollywood", "Honolulu", "Hoover",
    "High Point", "Hillsboro", "Hesperia", "Harlingen", "Hamilton",
    "Harrisburg", "Haverhill", "Hammond", "Hawthorne", "Hagerstown",
    "Hallandale Beach", "Hamburg", "Hanover", "Heidelberg", "Helsinki",
    "Haifa", "Havana", "Ho Chi Minh City", "Hanoi", "Hiroshima",
    "Hyderabad", "Halifax", "Hamilton", "Hull", "Harare", "Harbin",
    "Hefei", "Hangzhou", "Handan", "Homs", "Herat", "Hyderabad",
    # States
    "Hawaii", "Haryana", "Himachal Pradesh", "Hesse", "Hamburg",
    "Heilongjiang", "Henan", "Hubei", "Hunan", "Hainan", "Helmand",
    "Herat", "Hampshire", "Hertfordshire", "Herefordshire", "Huntingdonshire",
    "Hokkaido", "Hyogo", "Hiroshima", "Hamadan", "Hormozgan",
    # Continents
]
i = [
    # Countries
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Ivory Coast",
    # Cities
    "Indianapolis", "Irving", "Irvine", "Independence", "Inglewood",
    "Iowa City", "Ithaca", "Idaho Falls", "Imperial Beach", "Indio",
    "Inkster", "Ironton", "Issaquah", "Istanbul", "Izmir", "Isfahan",
    "Islamabad", "Izmir", "Ibadan", "Ilorin", "Ife", "Innsbruck",
    "Inverness", "Ipswich", "Islington", "Irkutsk", "Izhevsk", "Indore",
    "Imphal", "Itanagar", "Idukki", "Ilford", "Invercargill", "Iqaluit",
    "Iquique", "Ibague", "Ipatinga", "Imperatriz", "Iasi", "Izmir",
    # States
    "Iowa", "Idaho", "Illinois", "Indiana", "Ilocos", "Isabela",
    "Inner Mongolia", "Ionian Islands", "Isfahan", "Ilam", "Iowa",
    "Isle of Man", "Isle of Wight", "Inverclyde", "Inverness-shire",
    "Iwate", "Ibaraki", "Ishikawa", "Imo", "Isere", "Ille-et-Vilaine",
    # Continents
]
j = [
    # Countries
    "Jamaica", "Japan", "Jordan",
    # Cities
    "Jacksonville", "Jersey City", "Jackson", "Joliet", "Jersey City",
    "Jurupa Valley", "Janesville", "Johnson City", "Joplin", "Jackson",
    "Jacksonville Beach", "Janesville", "Jasper", "Jefferson City",
    "Jeddah", "Jerusalem", "Jaipur", "Jodhpur", "Jabalpur", "Jamshedpur",
    "Jakarta", "Jombang", "Jayapura", "Jember", "Jambi", "Johannesburg",
    "Juba", "Jinja", "Jeddah", "Jinan", "Jinzhou", "Jilin", "Jiujiang",
    "Jyvaskyla", "Joensuu", "Juarez", "Joinville", "Jundiai", "Juiz de Fora",
    "Jalapa", "Jacmel", "Jeju City", "Jeonju", "Jinju",
    # States
    "Jharkhand", "Jammu and Kashmir", "Jalisco", "Jiangsu", "Jiangxi",
    "Jilin", "Jujuy", "Jutland", "Jura", "Jeonbuk", "Jeju", "Johor",
    "Java", "Jambi", "Jawa Barat", "Jawa Tengah", "Jawa Timur",
    "Jerusalem District", "Jowzjan", "Jawzjan",
    # Continents
]
k = [
    # Countries
    "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan",
    "North Korea", "South Korea",
    # Cities
    "Kansas City", "Knoxville", "Killeen", "Kent", "Kenosha", "Kettering",
    "Kirkland", "Kissimmee", "Kalamazoo", "Kankakee", "Kennewick",
    "Kingston", "Kokomo", "Kyle", "Kabul", "Karachi", "Kathmandu",
    "Khartoum", "Kiev", "Kigali", "Kingston", "Kinshasa", "Kolkata",
    "Kuala Lumpur", "Kuwait City", "Kyoto", "Kobe", "Kumasi", "Kampala",
    "Kanpur", "Kochi", "Kozhikode", "Kurnool", "Kiel", "Kassel",
    "Karlsruhe", "Krakow", "Kazan", "Kharkiv", "Kaliningrad", "Krasnoyarsk",
    # States
    "Kansas", "Kentucky", "Karnataka", "Kerala", "Khyber Pakhtunkhwa",
    "Khorasan", "Kerman", "Kermanshah", "Khuzestan", "Kordestan",
    "Kangwon", "Kyonggi", "Kelantan", "Kedah", "Kuala Lumpur",
    "Kalimantan", "Kent", "Krasnodar", "Kurgan", "Kirov",
    # Continents
]
li = [
    # Countries
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg",
    # Cities
    "Los Angeles", "Las Vegas", "Louisville", "Laredo", "Lincoln",
    "Lubbock", "Lexington", "Long Beach", "Little Rock", "Lancaster",
    "Lakewood", "Lansing", "Largo", "Lawrence", "Lawton", "League City",
    "Lee's Summit", "Lewisville", "Lima", "Livonia", "London", "Liverpool",
    "Leeds", "Leicester", "Lyon", "Lille", "Lisbon", "Lagos", "Lahore",
    "Lucknow", "Ludhiana", "Lhasa", "Lome", "Libreville", "La Paz",
    "Lima", "Londrina", "Luanda", "Luxembourg City", "Ljubljana",
    # States
    "Louisiana", "Lazio", "Liguria", "Lombardy", "Limburg", "Limousin",
    "Languedoc", "Lorraine", "Lower Saxony", "Liaoning", "Limpopo",
    "Leinster", "Lancashire", "Lincolnshire", "Leicestershire", "Lothian",
    "Luzon", "Lampung", "Laikipia", "Loja", "La Rioja",
    # Continents
]
# WTH DOES AMBIGUOUS MEAN AND WHY IS MY CODE COMPILER SAYING THAT
m = [
    # Countries
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
    "Myanmar",
    # Cities
    "Memphis", "Mesa", "Miami", "Milwaukee", "Minneapolis", "Mobile",
    "Modesto", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta",
    "Madison", "Manchester", "McAllen", "McKinney", "Meridian", "Mesquite",
    "Midland", "Miramar", "Mission", "Mission Viejo", "Moreno Valley",
    "Madrid", "Milan", "Munich", "Manchester", "Marseille", "Moscow",
    "Montreal", "Melbourne", "Mumbai", "Manila", "Medina", "Mecca",
    "Marrakech", "Maputo", "Monrovia", "Mogadishu", "Montevideo",
    "Mexico City", "Monterrey", "Medellin", "Managua", "Minsk",
    # States
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Maharashtra", "Madhya Pradesh",
    "Manipur", "Meghalaya", "Mizoram", "Michoacan", "Morelos",
    "Mecklenburg-Vorpommern", "Mpumalanga", "Munster", "Malaga",
    "Murcia", "Marche", "Molise", "Minas Gerais", "Mato Grosso",
    # Continents
]
n = [
    # Countries
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway",
    # Cities
    "New York", "Newark", "Nashville", "Norfolk", "New Orleans",
    "Newport News", "Newton", "Niagara Falls", "Norman", "Norwalk",
    "Norwich", "Naperville", "Nashua", "New Bedford", "New Haven",
    "New Rochelle", "Newport", "Napa", "Naples", "Nice", "Nottingham",
    "Newcastle", "Nuremberg", "Nancy", "Nantes", "Nairobi", "N'Djamena",
    "Niamey", "Nouakchott", "New Delhi", "Nagpur", "Nashik", "Nanjing",
    "Nanning", "Ningbo", "Nagoya", "Naha", "Nouméa", "Nelspruit",
    # States
    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Nagaland", "Nuevo Leon",
    "Nayarit", "North Rhine-Westphalia", "Normandy", "Nord", "Northern Cape",
    "Northern Territory", "Newfoundland", "New South Wales",
    "Norte de Santander",
    "Ningxia", "Nunavut", "Northwest Territories", "Nordland", "Norrbotten",
    # Continents
    "North America",
]
o = [
    # Countries
    "Oman",
    # Cities
    "Oakland", "Oklahoma City", "Omaha", "Ontario", "Orange", "Orlando",
    "Overland Park", "Oxnard", "Oceanside", "Odessa", "Ogden", "Olathe",
    "Olympia", "Ontario", "Orem", "Orland Park", "Owensboro", "Oxford",
    "Oslo", "Osaka", "Odense", "Oulu", "Ottawa", "Oshawa", "Ostrava",
    "Oviedo", "Oldenburg", "Oberhausen", "Ouagadougou", "Onitsha",
    "Omdurman", "Oral", "Orenburg", "Omsk", "Oaxaca", "Oporto",
    # States
    "Ohio", "Oklahoma", "Oregon", "Odisha", "Oaxaca", "Overijssel",
    "Ostrobothnia", "Orkney", "Oxfordshire", "Orange Free State",
    "Oromia", "Osh", "Ourense", "Ontario", "Orissa",
    # Continents
    "Oceania",
]
p = [
    # Countries
    "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
    # Cities
    "Philadelphia", "Phoenix", "Pittsburgh", "Portland", "Plano",
    "Pembroke Pines", "Peoria", "Pomona", "Palmdale", "Pasadena",
    "Paterson", "Pearland", "Pembroke Pines", "Pompano Beach", "Portsmouth",
    "Providence", "Provo", "Pueblo", "Paris", "Prague", "Porto",
    "Palermo", "Padua", "Plymouth", "Preston", "Perth", "Panama City",
    "Port-au-Prince", "Phnom Penh", "Pyongyang", "Pune", "Patna",
    "Port Harcourt", "Pretoria", "Port Elizabeth", "Peshawar", "Palawan",
    # States
    "Pennsylvania", "Punjab", "Puducherry", "Puebla", "Pernambuco",
    "Para", "Piaui", "Parana", "Piedmont", "Provence", "Pomerania",
    "Podlaskie", "Prince Edward Island", "Punjab", "Paktia", "Panjshir",
    "Penang", "Perak", "Pahang", "Perlis", "Papua", "Pará",
    # Continents
]
q = [
    # Countries
    "Qatar",
    # Cities
    "Queens", "Quincy", "Quebec City", "Quito", "Qom", "Qingdao",
    "Quanzhou", "Quezon City", "Quilmes", "Qazvin", "Qena", "Qinghai",
    "Quilpue", "Quibdo", "Querétaro", "Quintana Roo", "Quetta",
    "Qardho", "Qandahar", "Qalqilya", "Qamishli", "Quba", "Qazvin",
    # States
    "Quebec", "Queensland", "Querétaro", "Quintana Roo", "Qinghai",
    "Qom", "Qazvin", "Qandahar", "Qazvin", "Quang Ninh", "Quang Nam",
    "Quang Tri", "Quang Binh", "Quang Ngai", "Qena", "Qassim",
    # Continents
]
r = [
    # Countries
    "Romania", "Russia", "Rwanda",
    # Cities
    "Raleigh", "Riverside", "Richmond", "Rochester", "Rockford",
    "Rancho Cucamonga",
    "Reno", "Rio Rancho", "Richardson", "Richmond", "Roanoke", "Rochester",
    "Rome", "Roseville", "Round Rock", "Rutland", "Reading", "Redditch",
    "Rome", "Rotterdam", "Reykjavik", "Riga", "Rhodes", "Rabat", "Riyadh",
    "Rawalpindi", "Rangoon", "Rostov-on-Don", "Rio de Janeiro", "Recife",
    "Ribeirao Preto", "Rosario", "Regina", "Richmond Hill", "Red Deer",
    "Rustenburg", "Rostock", "Regensburg", "Rennes", "Rimini", "Ravenna",
    # States
    "Rhode Island", "Rajasthan", "Rio de Janeiro", "Rio Grande do Sul",
    "Rio Grande do Norte", "Rondonia", "Roraima", "Rhineland-Palatinate",
    "Rioja", "Rhone", "Reunion", "Rogaland", "Rezekne", "Riga", "Roscommon",
    "Rutland", "Radnorshire", "Renfrewshire", "Ross-shire", "Roxburghshire",
    # Continents
]
s = [
    # Countries
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden",
    "Switzerland", "Syria",
    # Cities
    "San Antonio", "San Diego", "San Francisco", "San Jose", "Seattle",
    "Sacramento", "Santa Ana", "St. Louis", "St. Paul", "St. Petersburg",
    "Stockton", "Spokane", "Springfield", "Sterling Heights", "Sunnyvale",
    "Surprise", "Syracuse", "Salinas", "Savannah", "Scottsdale", "Shreveport",
    "Sydney", "Stockholm", "Stuttgart", "Seville", "Sheffield", "Southampton",
    "Seoul", "Shanghai", "Shenzhen", "Shenyang", "Shijiazhuang", "Suzhou",
    "Singapore", "Sydney", "Santiago", "Sao Paulo", "Salvador", "Santos",
    "Saskatoon", "Surrey", "Sudbury", "Sherbrooke", "Saint John",
    # States
    "South Carolina", "South Dakota", "Sikkim", "Sinaloa", "Sonora",
    "San Luis Potosi", "Saxony", "Schleswig-Holstein", "Saarland", "Sardinia",
    "Sicily", "Silesia", "Styria", "Salzburg", "Skane", "Smaland",
    "Shandong", "Shanxi", "Shaanxi", "Sichuan", "Sindh", "Sistan",
    "Somerset", "Staffordshire", "Suffolk", "Surrey", "Sussex", "Sutherland",
    # Continents
    "South America",
]
t = [
    # Countries
    "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    # Cities
    "Toledo", "Tucson", "Tulsa", "Tampa", "Tacoma", "Tallahassee", "Tempe",
    "Thornton", "Thousand Oaks", "Topeka", "Torrance", "Trenton", "Troy",
    "Tyler", "Tokyo", "Toronto", "Tehran", "Tel Aviv", "Tunis", "Tripoli",
    "Tirana", "Tbilisi", "Tashkent", "Thimphu", "Tegucigalpa", "Tijuana",
    "Turin", "Toulouse", "Thessaloniki", "The Hague", "Tampere", "Turku",
    "Tallinn", "Tartu", "Tianjin", "Taiyuan", "Tangshan", "Tainan",
    "Taichung", "Taipei", "Taguig", "Tijuana", "Tegucigalpa", "Tuxtla",
    # States
    "Tennessee", "Texas", "Tamil Nadu", "Telangana", "Tripura", "Tamaulipas",
    "Tlaxcala", "Tabasco", "Thuringia", "Tuscany", "Trentino", "Tyrol",
    "Troms", "Telemark", "Tianjin", "Tibet", "Turkmenistan", "Tatarstan",
    "Tver", "Tomsk", "Tyumen", "Tarapaca", "Tucuman", "Tierra del Fuego",
    # Continents
]
u = [
    # Countries
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan",
    # Cities
    "Union City", "Upland", "Upper Arlington", "Utica", "University City",
    "Urbandale", "Urbana", "Ulan Bator", "Utrecht", "Uppsala", "Umea",
    "Udine", "Ulsan", "Urumqi", "Ufa", "Ulyanovsk", "Underwood", "Ujjain",
    "Udaipur", "Ullal", "Unnao", "Ulhasnagar", "Upington", "Umtata",
    "Uberlandia", "Uruguaiana", "Ushuaia", "Ust-Kamenogorsk", "Urfa",
    "Usak", "Umm al-Quwain", "Umm Durman", "Upington", "Uyo",
    # States
    "Utah", "Uttar Pradesh", "Uttarakhand", "Ulster", "Umbria",
    "Upper Austria", "Uppsala", "Uusimaa", "Urals", "Udmurtia",
    "Ulyanovsk Oblast", "Ural", "Uvs", "Ungava", "Ucayali", "Utah",
    "Usulutan", "Ust-Orda", "Uvalde County", "Union County",
    # Continents
]
v = [
    # Countries
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    # Cities
    "Virginia Beach", "Vancouver", "Vallejo", "Ventura", "Victorville",
    "Visalia", "Vista", "Vacaville", "Valdosta", "Venice", "Vero Beach",
    "Victoria", "Vineland", "Virginia Beach", "Vienna", "Venice", "Verona",
    "Valencia", "Valladolid", "Vigo", "Victoria", "Vilnius", "Varna",
    "Vladivostok", "Volgograd", "Voronezh", "Vladikavkaz", "Vitebsk",
    "Vientiane", "Vijayawada", "Vadodara", "Varanasi", "Visakhapatnam",
    "Valparaiso", "Villa Carlos Paz", "Vitoria", "Vancouver", "Victoria",
    "Vernon", "Val-d'Or", "Vaughan", "Vereeniging", "Vanderbijlpark",
    # States
    "Vermont", "Virginia", "Victoria", "Valencia", "Valladolid",
    "Veneto", "Valle d'Aosta", "Vaud", "Valais", "Vasterbotten",
    "Varmland", "Vest-Agder", "Vestfold", "Vojvodina", "Vorarlberg",
    "Volgograd Oblast", "Vologda Oblast", "Vladimir Oblast", "Veracruz",
    "Vargas", "Vichada", "Vaupés", "Van", "Volyn", "Vinnytsia",
    # Continents
]
w = [
    # Countries
    # Cities
    "Washington", "Wichita", "Winston-Salem", "Worcester", "Warren",
    "Waterbury", "West Valley City", "Waco", "West Jordan", "West Palm Beach",
    "Waukegan", "Wheaton", "White Plains", "Wilmington", "Westminster",
    "Warwick", "Waterloo", "Waukesha", "Wayne", "Weymouth", "Whittier",
    "Warsaw", "Wroclaw", "Wuppertal", "Wurzburg", "Wiesbaden", "Wolfsburg",
    "Wellington", "Winnipeg", "Windsor", "Waterloo", "Whitehorse",
    "Wuhan", "Wenzhou", "Weifang", "Wuxi", "Wuhu", "Weihai", "Warangal",
    "Wollongong", "Windhoek", "Walvis Bay", "Wad Medani", "Warri",
    # States
    "Washington", "West Virginia", "Wisconsin", "Wyoming", "Western Australia",
    "Wales", "Westphalia", "Wurttemberg", "Western Cape", "Wallonia",
    "Warwickshire", "Westmorland", "Wiltshire", "Worcestershire",
    "West Bengal", "West Java", "West Kalimantan", "West Nusa Tenggara",
    "West Papua", "West Sumatra", "Waldviertel", "Weinviertel",
    # Continents
]
x = [
    # Countries
    # Cities
    "Xian", "Xiamen", "Xuzhou", "Xining", "Xinyang", "Xiangyang",
    "Xianyang", "Xinxiang", "Xiangtan", "Xinyu", "Xalapa", "Xochimilco",
    "Xavier", "Xenia", "Xerez", "Xanthi", "Xylokastro",
    # States
    "Xinjiang", "Xizang", "Xalapa", "Xianggang", "Xishuangbanna",
    # Continents
]
y = [
    # Countries
    "Yemen",
    # Cities
    "Yonkers", "Yakima", "Yuma", "York", "Youngstown", "Yorba Linda",
    "Yuba City", "Yokohama", "Yaoundé", "Yerevan", "Yekaterinburg",
    "Yaroslavl", "Yoshkar-Ola", "Yuzhno-Sakhalinsk", "Yelabuga", "Yalta",
    "Yamoussoukro", "Yangon", "Yantai", "Yancheng", "Yinchuan", "Yueyang",
    "Yichang", "Yiwu", "Yulin", "Yancheng", "Yanji", "York", "Yellowknife",
    "Yarmouth", "Yaounde", "Yopougon", "Yokosuka", "Yogyakarta",
    # States
    "Yukon", "Yunnan", "Yamal", "Yamalo-Nenets", "Yorkshire", "Yucatan",
    "Yaracuy", "Yoro", "Yap", "Yazd", "Yarsan", "Yonne", "Yvelines",
    # Continents
]
z = [
    # Countries
    "Zambia", "Zimbabwe",
    # Cities
    "Zurich", "Zagreb", "Zaragoza", "Zanzibar", "Zhengzhou", "Zhuhai",
    "Zibo", "Zhenjiang", "Zhanjiang", "Zunyi", "Zahedan", "Zanjan",
    "Zaria", "Zomba", "Zinder", "Zurich", "Zwolle", "Zenica", "Zilina",
    "Zielona Gora", "Zaporizhzhia", "Zhytomyr", "Zvolen", "Zamora",
    "Zacatecas", "Zipaquira", "Zacapa", "Zadar", "Zeeland", "Zug",
    # States
    "Zacatecas", "Zulia", "Zhejiang", "Zamfara", "Zanzibar", "Zeeland",
    "Zug", "Zurich", "Zabul", "Zanjan", "Zuid-Holland", "Zenica",
    "Zilina", "Zlín", "Zala", "Zemplén", "Zaporizhzhia", "Zhytomyr",
    # Continents
]


# Combine all lists into alol
alol = []
alol.extend(a)
alol.extend(b)
alol.extend(c)
alol.extend(d)
alol.extend(e)
alol.extend(f)
alol.extend(g)
alol.extend(h)
alol.extend(i)
alol.extend(j)
alol.extend(k)
alol.extend(li)
alol.extend(m)
alol.extend(n)
alol.extend(o)
alol.extend(p)
alol.extend(q)
alol.extend(r)
alol.extend(s)
alol.extend(t)
alol.extend(u)
alol.extend(v)
alol.extend(w)
alol.extend(x)
alol.extend(y)
alol.extend(z)

# Create the atlas dictionary
atlas = {
    "a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h,
    "i": i, "j": j, "k": k, "l": li, "m": m, "n": n, "o": o, "p": p,
    "q": q, "r": r, "s": s, "t": t, "u": u, "v": v, "w": w, "x": x,
    "y": y, "z": z
}

# Add uppercase keys to atlas
for key in list(atlas.keys()):
    atlas[key.upper()] = atlas[key]

# Global game state variables
llu = None
flu = None
llb = "s"
out = "placeholder"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='place')
async def place_command(ctx, *, place: str):
    global alol, llu, llb, flu, atlas, out

    # Use the provided place as input
    inp = place.strip()
    llu = inp[-1].lower()
    flu = inp[0].lower()

    if llb is None:
        llb = "s"

    if inp in alol:
        await ctx.send(f"Valid place: {inp}")
        alol.remove(inp)
        atlas[flu].remove(inp)
        
        if llu in atlas:
            out = atlas[llu][0]
            # Ensure the selected place is still available
            if out not in atlas[llu]:
                try:
                    out = atlas[llu][1]
                except IndexError:
                    await ctx.send("No more places available for this letter!")
                    return
            await ctx.send(f"Bot's response: {out}")
            atlas[llu].remove(out)
            alol.remove(out)
            llb = out[-1].lower()
            await ctx.send(f"Next place must start with: {llb.upper()}")
        else:
            await ctx.send("No places available for this letter!")
    else:
        await ctx.send(f"Invalid place: {inp}")

    # Check if any list in atlas is empty
    if any(len(lst) == 0 for lst in atlas.values()):
        await ctx.send("Game Over! You Win!")
        # Reset game state if desired
        # alol.extend(a + b + c + ... + z)  # Reset alol
        # atlas = {...}  # Reset atlas
        # llu, flu, llb, out = None, None, "s", "placeholder"

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
bot.run('YOUR_BOT_TOKEN')