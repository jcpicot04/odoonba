# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
from odoo.exceptions import ValidationError
from datetime import datetime
import random
import re
import base64

class equipos(models.Model):
    _name = 'equipos.equipos'
    _description = 'Equipos'

    @api.model
    def create(self, values):
        equipo = super(equipos, self).create(values)
        print(values)
        name_team = equipo.name
        names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley", "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun", "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan", "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz", "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee", "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody", "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan", "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "Caiden-Paul", "Caidyn", "Caie", "Cailaen", "Cailean", "Caileb-John", "Cailin", "Cain", "Caine", "Cairn", "Cal", "Calan", "Calder", "Cale", "Calean", "Caleb", "Calen", "Caley", "Calib", "Calin", "Callahan", "Callan", "Callan-Adam", "Calley", "Callie", "Callin", "Callum", "Callun", "Callyn", "Calum", "Calum-James", "Calvin", "Cambell", "Camerin", "Cameron", "Campbel", "Campbell", "Camron", "Caolain", "Caolan", "Carl", "Carlo", "Carlos", "Carrich", "Carrick", "Carson", "Carter", "Carwyn", "Casey", "Casper", "Cassy", "Cathal", "Cator", "Cavan", "Cayden", "Cayden-Robert", "Cayden-Tiamo", "Ceejay", "Ceilan", "Ceiran", "Ceirin", "Ceiron", "Cejay", "Celik", "Cephas", "Cesar", "Cesare", "Chad", "Chaitanya", "Chang-Ha", "Charles", "Charley", "Charlie", "Charly", "Chase", "Che", "Chester", "Chevy", "Chi", "Chibudom", "Chidera", "Chimsom", "Chin", "Chintu", "Chiqal", "Chiron", "Chris", "Chris-Daniel", "Chrismedi", "Christian", "Christie", "Christoph", "Christopher", "Christopher-Lee", "Christy", "Chu", "Chukwuemeka", "Cian", "Ciann", "Ciar", "Ciaran", "Ciarian", "Cieran", "Cillian", "Cillin", "Cinar", "CJ", "C-Jay", "Clark", "Clarke", "Clayton", "Clement", "Clifford", "Clyde", "Cobain", "Coban", "Coben", "Cobi", "Cobie", "Coby", "Codey", "Codi", "Codie", "Cody", "Cody-Lee", "Coel", "Cohan", "Cohen", "Colby", "Cole", "Colin", "Coll", "Colm", "Colt", "Colton", "Colum", "Colvin", "Comghan", "Conal", "Conall", "Conan", "Conar", "Conghaile", "Conlan", "Conley", "Conli", "Conlin", "Conlly", "Conlon", "Conlyn", "Connal", "Connall", "Connan", "Connar", "Connel", "Connell", "Conner", "Connolly", "Connor", "Connor-David", "Conor", "Conrad", "Cooper", "Copeland", "Coray", "Corben", "Corbin", "Corey", "Corey-James", "Corey-Jay", "Cori", "Corie", "Corin", "Cormac", "Cormack", "Cormak", "Corran", "Corrie", "Cory", "Cosmo", "Coupar", "Craig", "Craig-James", "Crawford", "Creag", "Crispin", "Cristian", "Crombie", "Cruiz", "Cruz", "Cuillin", "Cullen", "Cullin", "Curtis", "Cyrus", "Daanyaal", "Daegan", "Daegyu", "Dafydd", "Dagon", "Dailey", "Daimhin", "Daithi", "Dakota", "Daksh", "Dale", "Dalong", "Dalton", "Damian", "Damien", "Damon", "Dan", "Danar", "Dane", "Danial", "Daniel", "Daniele", "Daniel-James", "Daniels", "Daniil", "Danish", "Daniyal", "Danniel", "Danny", "Dante", "Danyal", "Danyil", "Danys", "Daood", "Dara", "Darach", "Daragh", "Darcy", "D'arcy", "Dareh", "Daren", "Darien", "Darius", "Darl", "Darn", "Darrach", "Darragh", "Darrel", "Darrell", "Darren", "Darrie", "Darrius", "Darroch", "Darryl", "Darryn", "Darwyn", "Daryl", "Daryn", "Daud", "Daumantas", "Davi", "David", "David-Jay", "David-Lee", "Davie", "Davis", "Davy", "Dawid", "Dawson", "Dawud", "Dayem", "Daymian", "Deacon", "Deagan", "Dean", "Deano", "Decklan", "Declain", "Declan", "Declyan", "Declyn", "Dedeniseoluwa", "Deecan", "Deegan", "Deelan", "Deklain-Jaimes", "Del", "Demetrius", "Denis", "Deniss", "Dennan", "Dennin", "Dennis", "Denny", "Dennys", "Denon", "Denton", "Denver", "Denzel", "Deon", "Derek", "Derick", "Derin", "Dermot", "Derren", "Derrie", "Derrin", "Derron", "Derry", "Derryn", "Deryn", "Deshawn", "Desmond", "Dev", "Devan", "Devin", "Devlin", "Devlyn", "Devon", "Devrin", "Devyn", "Dex", "Dexter", "Dhani", "Dharam", "Dhavid", "Dhyia", "Diarmaid", "Diarmid", "Diarmuid", "Didier", "Diego", "Diesel", "Diesil", "Digby", "Dilan", "Dilano", "Dillan", "Dillon", "Dilraj", "Dimitri", "Dinaras", "Dion", "Dissanayake", "Dmitri", "Doire", "Dolan", "Domanic", "Domenico", "Domhnall", "Dominic", "Dominick", "Dominik", "Donald", "Donnacha", "Donnie", "Dorian", "Dougal", "Douglas", "Dougray", "Drakeo", "Dre", "Dregan", "Drew", "Dugald", "Duncan", "Duriel", "Dustin", "Dylan", "Dylan-Jack", "Dylan-James", "Dylan-John", "Dylan-Patrick", "Dylin", "Dyllan", "Dyllan-James", "Dyllon", "Eadie", "Eagann", "Eamon", "Eamonn", "Eason", "Eassan", "Easton", "Ebow", "Ed", "Eddie", "Eden", "Ediomi", "Edison", "Eduardo", "Eduards", "Edward", "Edwin", "Edwyn", "Eesa", "Efan", "Efe", "Ege", "Ehsan", "Ehsen", "Eiddon", "Eidhan", "Eihli", "Eimantas", "Eisa", "Eli", "Elias", "Elijah", "Eliot", "Elisau", "Eljay", "Eljon", "Elliot", "Elliott", "Ellis", "Ellisandro", "Elshan", "Elvin", "Elyan", "Emanuel", "Emerson", "Emil", "Emile", "Emir", "Emlyn", "Emmanuel", "Emmet", "Eng", "Eniola", "Enis", "Ennis", "Enrico", "Enrique", "Enzo", "Eoghain", "Eoghan", "Eoin", "Eonan", "Erdehan", "Eren", "Erencem", "Eric", "Ericlee", "Erik", "Eriz", "Ernie-Jacks", "Eroni", "Eryk", "Eshan", "Essa", "Esteban", "Ethan", "Etienne", "Etinosa", "Euan", "Eugene", "Evan", "Evann", "Ewan", "Ewen", "Ewing", "Exodi", "Ezekiel", "Ezra", "Fabian", "Fahad", "Faheem", "Faisal", "Faizaan", "Famara", "Fares", "Farhaan", "Farhan", "Farren", "Farzad", "Fauzaan", "Favour", "Fawaz", "Fawkes", "Faysal", "Fearghus", "Feden", "Felix", "Fergal", "Fergie", "Fergus", "Ferre", "Fezaan", "Fiachra", "Fikret", "Filip", "Filippo", "Finan", "Findlay", "Findlay-James", "Findlie", "Finlay", "Finley", "Finn", "Finnan", "Finnean", "Finnen", "Finnlay", "Finnley", "Fintan", "Fionn", "Firaaz", "Fletcher", "Flint", "Florin", "Flyn", "Flynn", "Fodeba", "Folarinwa", "Forbes", "Forgan", "Forrest", "Fox", "Francesco", "Francis", "Francisco", "Franciszek", "Franco", "Frank", "Frankie", "Franklin", "Franko", "Fraser", "Frazer", "Fred", "Freddie", "Frederick", "Fruin", "Fyfe", "Fyn", "Fynlay", "Fynn", "Gabriel", "Gallagher", "Gareth", "Garren", "Garrett", "Garry", "Gary", "Gavin", "Gavin-Lee", "Gene", "Geoff", "Geoffrey", "Geomer", "Geordan", "Geordie", "George", "Georgia", "Georgy", "Gerard", "Ghyll", "Giacomo", "Gian", "Giancarlo", "Gianluca", "Gianmarco", "Gideon", "Gil", "Gio", "Girijan", "Girius", "Gjan", "Glascott", "Glen", "Glenn", "Gordon", "Grady", "Graeme", "Graham", "Grahame", "Grant", "Grayson", "Greg", "Gregor", "Gregory", "Greig", "Griffin", "Griffyn", "Grzegorz", "Guang", "Guerin", "Guillaume", "Gurardass", "Gurdeep", "Gursees", "Gurthar", "Gurveer", "Gurwinder", "Gus", "Gustav", "Guthrie", "Guy", "Gytis", "Habeeb", "Hadji", "Hadyn", "Hagun", "Haiden", "Haider", "Hamad", "Hamid", "Hamish", "Hamza", "Hamzah", "Han", "Hansen", "Hao", "Hareem", "Hari", "Harikrishna", "Haris", "Harish", "Harjeevan", "Harjyot", "Harlee", "Harleigh", "Harley", "Harman", "Harnek", "Harold", "Haroon", "Harper", "Harri", "Harrington", "Harris", "Harrison", "Harry", "Harvey", "Harvie", "Harvinder", "Hasan", "Haseeb", "Hashem", "Hashim", "Hassan", "Hassanali", "Hately", "Havila", "Hayden", "Haydn", "Haydon", "Haydyn", "Hcen", "Hector", "Heddle", "Heidar", "Heini", "Hendri", "Henri", "Henry", "Herbert", "Heyden", "Hiro", "Hirvaansh", "Hishaam", "Hogan", "Honey", "Hong", "Hope", "Hopkin", "Hosea", "Howard", "Howie", "Hristomir", "Hubert", "Hugh", "Hugo", "Humza", "Hunter", "Husnain", "Hussain", "Hussan", "Hussnain", "Hussnan", "Hyden", "I", "Iagan", "Iain", "Ian", "Ibraheem", "Ibrahim", "Idahosa", "Idrees", "Idris", "Iestyn", "Ieuan", "Igor", "Ihtisham", "Ijay", "Ikechukwu", "Ikemsinachukwu", "Ilyaas", "Ilyas", "Iman", "Immanuel", "Inan", "Indy", "Ines", "Innes", "Ioannis", "Ireayomide", "Ireoluwa", "Irvin", "Irvine", "Isa", "Isaa", "Isaac", "Isaiah", "Isak", "Isher", "Ishwar", "Isimeli", "Isira", "Ismaeel", "Ismail", "Israel", "Issiaka", "Ivan", "Ivar", "Izaak", "J", "Jaay", "Jac", "Jace", "Jack", "Jacki", "Jackie", "Jack-James", "Jackson", "Jacky", "Jacob", "Jacques", "Jad", "Jaden", "Jadon", "Jadyn", "Jae", "Jagat", "Jago", "Jaheim", "Jahid", "Jahy", "Jai", "Jaida", "Jaiden", "Jaidyn", "Jaii", "Jaime", "Jai-Rajaram", "Jaise", "Jak", "Jake", "Jakey", "Jakob", "Jaksyn", "Jakub", "Jamaal", "Jamal", "Jameel", "Jameil", "James", "James-Paul", "Jamey", "Jamie", "Jan", "Jaosha", "Jardine", "Jared", "Jarell", "Jarl", "Jarno", "Jarred", "Jarvi", "Jasey-Jay", "Jasim", "Jaskaran", "Jason", "Jasper", "Jaxon", "Jaxson", "Jay", "Jaydan", "Jayden", "Jayden-James", "Jayden-Lee", "Jayden-Paul", "Jayden-Thomas", "Jaydn", "Jaydon", "Jaydyn", "Jayhan", "Jay-Jay", "Jayke", "Jaymie", "Jayse", "Jayson", "Jaz", "Jazeb", "Jazib", "Jazz", "Jean", "Jean-Lewis", "Jean-Pierre", "Jebadiah", "Jed", "Jedd", "Jedidiah", "Jeemie", "Jeevan", "Jeffrey", "Jensen", "Jenson", "Jensyn", "Jeremy", "Jerome", "Jeronimo", "Jerrick", "Jerry", "Jesse", "Jesuseun", "Jeswin", "Jevan", "Jeyun", "Jez", "Jia", "Jian", "Jiao", "Jimmy", "Jincheng", "JJ", "Joaquin", "Joash", "Jock", "Jody", "Joe", "Joeddy", "Joel", "Joey", "Joey-Jack", "Johann", "Johannes", "Johansson", "John", "Johnathan", "Johndean", "Johnjay", "John-Michael", "Johnnie", "Johnny", "Johnpaul", "John-Paul", "John-Scott", "Johnson", "Jole", "Jomuel", "Jon", "Jonah", "Jonatan", "Jonathan", "Jonathon", "Jonny", "Jonothan", "Jon-Paul", "Jonson", "Joojo", "Jordan", "Jordi", "Jordon", "Jordy", "Jordyn", "Jorge", "Joris", "Jorryn", "Josan", "Josef", "Joseph", "Josese", "Josh", "Joshiah", "Joshua", "Josiah", "Joss", "Jostelle", "Joynul", "Juan", "Jubin", "Judah", "Jude", "Jules", "Julian", "Julien", "Jun", "Junior", "Jura", "Justan", "Justin", "Justinas", "Kaan", "Kabeer", "Kabir", "Kacey", "Kacper", "Kade", "Kaden", "Kadin", "Kadyn", "Kaeden", "Kael", "Kaelan", "Kaelin", "Kaelum", "Kai", "Kaid", "Kaidan", "Kaiden", "Kaidinn", "Kaidyn", "Kaileb", "Kailin", "Kain", "Kaine", "Kainin", "Kainui", "Kairn", "Kaison", "Kaiwen", "Kajally", "Kajetan", "Kalani", "Kale", "Kaleb", "Kaleem", "Kal-el", "Kalen", "Kalin", "Kallan", "Kallin", "Kalum", "Kalvin", "Kalvyn", "Kameron", "Kames", "Kamil", "Kamran", "Kamron", "Kane", "Karam", "Karamvir", "Karandeep", "Kareem", "Karim", "Karimas", "Karl", "Karol", "Karson", "Karsyn", "Karthikeya", "Kasey", "Kash", "Kashif", "Kasim", "Kasper", "Kasra", "Kavin", "Kayam", "Kaydan", "Kayden", "Kaydin", "Kaydn", "Kaydyn", "Kaydyne", "Kayleb", "Kaylem", "Kaylum", "Kayne", "Kaywan", "Kealan", "Kealon", "Kean", "Keane", "Kearney", "Keatin", "Keaton", "Keavan", "Keayn", "Kedrick", "Keegan", "Keelan", "Keelin", "Keeman", "Keenan", "Keenan-Lee", "Keeton", "Kehinde", "Keigan", "Keilan", "Keir", "Keiran", "Keiren", "Keiron", "Keiryn", "Keison", "Keith", "Keivlin", "Kelam", "Kelan", "Kellan", "Kellen", "Kelso", "Kelum", "Kelvan", "Kelvin", "Ken", "Kenan", "Kendall", "Kendyn", "Kenlin", "Kenneth", "Kensey", "Kenton", "Kenyon", "Kenzeigh", "Kenzi", "Kenzie", "Kenzo", "Kenzy", "Keo", "Ker", "Kern", "Kerr", "Kevan", "Kevin", "Kevyn", "Kez", "Khai", "Khalan", "Khaleel", "Khaya", "Khevien", "Khizar", "Khizer", "Kia", "Kian", "Kian-James", "Kiaran", "Kiarash", "Kie", "Kiefer", "Kiegan", "Kienan", "Kier", "Kieran", "Kieran-Scott", "Kieren", "Kierin", "Kiern", "Kieron", "Kieryn", "Kile", "Killian", "Kimi", "Kingston", "Kinneil", "Kinnon", "Kinsey", "Kiran", "Kirk", "Kirwin", "Kit", "Kiya", "Kiyonari", "Kjae", "Klein", "Klevis", "Kobe", "Kobi", "Koby", "Koddi", "Koden", "Kodi", "Kodie", "Kody", "Kofi", "Kogan", "Kohen", "Kole", "Konan", "Konar", "Konnor", "Konrad", "Koray", "Korben", "Korbyn", "Korey", "Kori", "Korrin", "Kory", "Koushik", "Kris", "Krish", "Krishan", "Kriss", "Kristian", "Kristin", "Kristofer", "Kristoffer", "Kristopher", "Kruz", "Krzysiek", "Krzysztof", "Ksawery", "Ksawier", "Kuba", "Kurt", "Kurtis", "Kurtis-Jae", "Kyaan", "Kyan", "Kyde", "Kyden", "Kye", "Kyel", "Kyhran", "Kyie", "Kylan", "Kylar", "Kyle", "Kyle-Derek", "Kylian", "Kym", "Kynan", "Kyral", "Kyran", "Kyren", "Kyrillos", "Kyro", "Kyron", "Kyrran", "Lachlainn", "Lachlan", "Lachlann", "Lael", "Lagan", "Laird", "Laison", "Lakshya", "Lance", "Lancelot", "Landon", "Lang", "Lasse", "Latif", "Lauchlan", "Lauchlin", "Laughlan", "Lauren", "Laurence", "Laurie", "Lawlyn", "Lawrence", "Lawrie", "Lawson", "Layne", "Layton", "Lee", "Leigh", "Leigham", "Leighton", "Leilan", "Leiten", "Leithen", "Leland", "Lenin", "Lennan", "Lennen", "Lennex", "Lennon", "Lennox", "Lenny", "Leno", "Lenon", "Lenyn", "Leo", "Leon", "Leonard", "Leonardas", "Leonardo", "Lepeng", "Leroy", "Leven", "Levi", "Levon", "Levy", "Lewie", "Lewin", "Lewis", "Lex", "Leydon", "Leyland", "Leylann", "Leyton", "Liall", "Liam", "Liam-Stephen", "Limo", "Lincoln", "Lincoln-John", "Lincon", "Linden", "Linton", "Lionel", "Lisandro", "Litrell", "Liyonela-Elam", "LLeyton", "Lliam", "Lloyd", "Lloyde", "Loche", "Lochlan", "Lochlann", "Lochlan-Oliver", "Lock", "Lockey", "Logan", "Logann", "Logan-Rhys", "Loghan", "Lokesh", "Loki", "Lomond", "Lorcan", "Lorenz", "Lorenzo", "Lorne", "Loudon", "Loui", "Louie", "Louis", "Loukas", "Lovell", "Luc", "Luca", "Lucais", "Lucas", "Lucca", "Lucian", "Luciano", "Lucien", "Lucus", "Luic", "Luis", "Luk", "Luka", "Lukas", "Lukasz", "Luke", "Lukmaan", "Luqman", "Lyall", "Lyle", "Lyndsay", "Lysander", "Maanav", "Maaz", "Mac", "Macallum", "Macaulay", "Macauley", "Macaully", "Machlan", "Maciej", "Mack", "Mackenzie", "Mackenzy", "Mackie", "Macsen", "Macy", "Madaki", "Maddison", "Maddox", "Madison", "Madison-Jake", "Madox", "Mael", "Magnus", "Mahan", "Mahdi", "Mahmoud", "Maias", "Maison", "Maisum", "Maitlind", "Majid", "Makensie", "Makenzie", "Makin", "Maksim", "Maksymilian", "Malachai", "Malachi", "Malachy", "Malakai", "Malakhy", "Malcolm", "Malik", "Malikye", "Malo", "Ma'moon", "Manas", "Maneet", "Manmohan", "Manolo", "Manson", "Mantej", "Manuel", "Manus", "Marc", "Marc-Anthony", "Marcel", "Marcello", "Marcin", "Marco", "Marcos", "Marcous", "Marcquis", "Marcus", "Mario", "Marios", "Marius", "Mark", "Marko", "Markus", "Marley", "Marlin", "Marlon", "Maros", "Marshall", "Martin", "Marty", "Martyn", "Marvellous", "Marvin", "Marwan", "Maryk", "Marzuq", "Mashhood", "Mason", "Mason-Jay", "Masood", "Masson", "Matas", "Matej", "Mateusz", "Mathew", "Mathias", "Mathu", "Mathuyan", "Mati", "Matt", "Matteo", "Matthew", "Matthew-William", "Matthias", "Max", "Maxim", "Maximilian", "Maximillian", "Maximus", "Maxwell", "Maxx", "Mayeul", "Mayson", "Mazin", "Mcbride", "McCaulley", "McKade", "McKauley", "McKay", "McKenzie", "McLay", "Meftah", "Mehmet", "Mehraz", "Meko", "Melville", "Meshach", "Meyzhward", "Micah", "Michael", "Michael-Alexander", "Michael-James", "Michal", "Michat", "Micheal", "Michee", "Mickey", "Miguel", "Mika", "Mikael", "Mikee", "Mikey", "Mikhail", "Mikolaj", "Miles", "Millar", "Miller", "Milo", "Milos", "Milosz", "Mir", "Mirza", "Mitch", "Mitchel", "Mitchell", "Moad", "Moayd", "Mobeen", "Modoulamin", "Modu", "Mohamad", "Mohamed", "Mohammad", "Mohammad-Bilal", "Mohammed", "Mohanad", "Mohd", "Momin", "Momooreoluwa", "Montague", "Montgomery", "Monty", "Moore", "Moosa", "Moray", "Morgan", "Morgyn", "Morris", "Morton", "Moshy", "Motade", "Moyes", "Msughter", "Mueez", "Muhamadjavad", "Muhammad", "Muhammed", "Muhsin", "Muir", "Munachi", "Muneeb", "Mungo", "Munir", "Munmair", "Munro", "Murdo", "Murray", "Murrough", "Murry", "Musa", "Musse", "Mustafa", "Mustapha", "Muzammil", "Muzzammil", "Mykie", "Myles", "Mylo", "Nabeel", "Nadeem", "Nader", "Nagib", "Naif", "Nairn", "Narvic", "Nash", "Nasser", "Nassir", "Natan", "Nate", "Nathan", "Nathanael", "Nathanial", "Nathaniel", "Nathan-Rae", "Nawfal", "Nayan", "Neco", "Neil", "Nelson", "Neo", "Neshawn", "Nevan", "Nevin", "Ngonidzashe", "Nial", "Niall", "Nicholas", "Nick", "Nickhill", "Nicki", "Nickson", "Nicky", "Nico", "Nicodemus", "Nicol", "Nicolae", "Nicolas", "Nidhish", "Nihaal", "Nihal", "Nikash", "Nikhil", "Niki", "Nikita", "Nikodem", "Nikolai", "Nikos", "Nilav", "Niraj", "Niro", "Niven", "Noah", "Noel", "Nolan", "Noor", "Norman", "Norrie", "Nuada", "Nyah", "Oakley", "Oban", "Obieluem", "Obosa", "Odhran", "Odin", "Odynn", "Ogheneochuko", "Ogheneruno", "Ohran", "Oilibhear", "Oisin", "Ojima-Ojo", "Okeoghene", "Olaf", "Ola-Oluwa", "Olaoluwapolorimi", "Ole", "Olie", "Oliver", "Olivier", "Oliwier", "Ollie", "Olurotimi", "Oluwadamilare", "Oluwadamiloju", "Oluwafemi", "Oluwafikunayomi", "Oluwalayomi", "Oluwatobiloba", "Oluwatoni", "Omar", "Omri", "Oran", "Orin", "Orlando", "Orley", "Orran", "Orrick", "Orrin", "Orson", "Oryn", "Oscar", "Osesenagha", "Oskar", "Ossian", "Oswald", "Otto", "Owain", "Owais", "Owen", "Owyn", "Oz", "Ozzy", "Pablo", "Pacey", "Padraig", "Paolo", "Pardeepraj", "Parkash", "Parker", "Pascoe", "Pasquale", "Patrick", "Patrick-John", "Patrikas", "Patryk", "Paul", "Pavit", "Pawel", "Pawlo", "Pearce", "Pearse", "Pearsen", "Pedram", "Pedro", "Peirce", "Peiyan", "Pele", "Peni", "Peregrine", "Peter", "Phani", "Philip", "Philippos", "Phinehas", "Phoenix", "Phoevos", "Pierce", "Pierre-Antoine", "Pieter", "Pietro", "Piotr", "Porter", "Prabhjoit", "Prabodhan", "Praise", "Pranav", "Pravin", "Precious", "Prentice", "Presley", "Preston", "Preston-Jay", "Prinay", "Prince", "Prithvi", "Promise", "Puneetpaul", "Pushkar", "Qasim", "Qirui", "Quinlan", "Quinn", "Radmiras", "Raees", "Raegan", "Rafael", "Rafal", "Rafferty", "Rafi", "Raheem", "Rahil", "Rahim", "Rahman", "Raith", "Raithin", "Raja", "Rajab-Ali", "Rajan", "Ralfs", "Ralph", "Ramanas", "Ramit", "Ramone", "Ramsay", "Ramsey", "Rana", "Ranolph", "Raphael", "Rasmus", "Rasul", "Raul", "Raunaq", "Ravin", "Ray", "Rayaan", "Rayan", "Rayane", "Rayden", "Rayhan", "Raymond", "Rayne", "Rayyan", "Raza", "Reace", "Reagan", "Reean", "Reece", "Reed", "Reegan", "Rees", "Reese", "Reeve", "Regan", "Regean", "Reggie", "Rehaan", "Rehan", "Reice", "Reid", "Reigan", "Reilly", "Reily", "Reis", "Reiss", "Remigiusz", "Remo", "Remy", "Ren", "Renars", "Reng", "Rennie", "Reno", "Reo", "Reuben", "Rexford", "Reynold", "Rhein", "Rheo", "Rhett", "Rheyden", "Rhian", "Rhoan", "Rholmark", "Rhoridh", "Rhuairidh", "Rhuan", "Rhuaridh", "Rhudi", "Rhy", "Rhyan", "Rhyley", "Rhyon", "Rhys", "Rhys-Bernard", "Rhyse", "Riach", "Rian", "Ricards", "Riccardo", "Ricco", "Rice", "Richard", "Richey", "Richie", "Ricky", "Rico", "Ridley", "Ridwan", "Rihab", "Rihan", "Rihards", "Rihonn", "Rikki", "Riley", "Rio", "Rioden", "Rishi", "Ritchie", "Rivan", "Riyadh", "Riyaj", "Roan", "Roark", "Roary", "Rob", "Robbi", "Robbie", "Robbie-lee", "Robby", "Robert", "Robert-Gordon", "Robertjohn", "Robi", "Robin", "Rocco", "Roddy", "Roderick", "Rodrigo", "Roen", "Rogan", "Roger", "Rohaan", "Rohan", "Rohin", "Rohit", "Rokas", "Roman", "Ronald", "Ronan", "Ronan-Benedict", "Ronin", "Ronnie", "Rooke", "Roray", "Rori", "Rorie", "Rory", "Roshan", "Ross", "Ross-Andrew", "Rossi", "Rowan", "Rowen", "Roy", "Ruadhan", "Ruaidhri", "Ruairi", "Ruairidh", "Ruan", "Ruaraidh", "Ruari", "Ruaridh", "Ruben", "Rubhan", "Rubin", "Rubyn", "Rudi", "Rudy", "Rufus", "Rui", "Ruo", "Rupert", "Ruslan", "Russel", "Russell", "Ryaan", "Ryan", "Ryan-Lee", "Ryden", "Ryder", "Ryese", "Ryhs", "Rylan", "Rylay", "Rylee", "Ryleigh", "Ryley", "Rylie", "Ryo", "Ryszard", "Saad", "Sabeen", "Sachkirat", "Saffi", "Saghun", "Sahaib", "Sahbian", "Sahil", "Saif", "Saifaddine", "Saim", "Sajid", "Sajjad", "Salahudin", "Salman", "Salter", "Salvador", "Sam", "Saman", "Samar", "Samarjit", "Samatar", "Sambrid", "Sameer", "Sami", "Samir", "Sami-Ullah", "Samual", "Samuel", "Samuela", "Samy", "Sanaullah", "Sandro", "Sandy", "Sanfur", "Sanjay", "Santiago", "Santino", "Satveer", "Saul", "Saunders", "Savin", "Sayad", "Sayeed", "Sayf", "Scot", "Scott", "Scott-Alexander", "Seaan", "Seamas", "Seamus", "Sean", "Seane", "Sean-James", "Sean-Paul", "Sean-Ray", "Seb", "Sebastian", "Sebastien", "Selasi", "Seonaidh", "Sephiroth", "Sergei", "Sergio", "Seth", "Sethu", "Seumas", "Shaarvin", "Shadow", "Shae", "Shahmir", "Shai", "Shane", "Shannon", "Sharland", "Sharoz", "Shaughn", "Shaun", "Shaunpaul", "Shaun-Paul", "Shaun-Thomas", "Shaurya", "Shaw", "Shawn", "Shawnpaul", "Shay", "Shayaan", "Shayan", "Shaye", "Shayne", "Shazil", "Shea", "Sheafan", "Sheigh", "Shenuk", "Sher", "Shergo", "Sheriff", "Sherwyn", "Shiloh", "Shiraz", "Shreeram", "Shreyas", "Shyam", "Siddhant", "Siddharth", "Sidharth", "Sidney", "Siergiej", "Silas", "Simon", "Sinai", "Skye", "Sofian", "Sohaib", "Sohail", "Soham", "Sohan", "Sol", "Solomon", "Sonneey", "Sonni", "Sonny", "Sorley", "Soul", "Spencer", "Spondon", "Stanislaw", "Stanley", "Stefan", "Stefano", "Stefin", "Stephen", "Stephenjunior", "Steve", "Steven", "Steven-lee", "Stevie", "Stewart", "Stewarty", "Strachan", "Struan", "Stuart", "Su", "Subhaan", "Sudais", "Suheyb", "Suilven", "Sukhi", "Sukhpal", "Sukhvir", "Sulayman", "Sullivan", "Sultan", "Sung", "Sunny", "Suraj", "Surien", "Sweyn", "Syed", "Sylvain", "Symon", "Szymon", "Tadd", "Taddy", "Tadhg", "Taegan", "Taegen", "Tai", "Tait", "Taiwo", "Talha", "Taliesin", "Talon", "Talorcan", "Tamar", "Tamiem", "Tammam", "Tanay", "Tane", "Tanner", "Tanvir", "Tanzeel", "Taonga", "Tarik", "Tariq-Jay", "Tate", "Taylan", "Taylar", "Tayler", "Taylor", "Taylor-Jay", "Taylor-Lee", "Tayo", "Tayyab", "Tayye", "Tayyib", "Teagan", "Tee", "Teejay", "Tee-jay", "Tegan", "Teighen", "Teiyib", "Te-Jay", "Temba", "Teo", "Teodor", "Teos", "Terry", "Teydren", "Theo", "Theodore", "Thiago", "Thierry", "Thom", "Thomas", "Thomas-Jay", "Thomson", "Thorben", "Thorfinn", "Thrinei", "Thumbiko", "Tiago", "Tian", "Tiarnan", "Tibet", "Tieran", "Tiernan", "Timothy", "Timucin", "Tiree", "Tisloh", "Titi", "Titus", "Tiylar", "TJ", "Tjay", "T-Jay", "Tobey", "Tobi", "Tobias", "Tobie", "Toby", "Todd", "Tokinaga", "Toluwalase", "Tom", "Tomas", "Tomasz", "Tommi-Lee", "Tommy", "Tomson", "Tony", "Torin", "Torquil", "Torran", "Torrin", "Torsten", "Trafford", "Trai", "Travis", "Tre", "Trent", "Trey", "Tristain", "Tristan", "Troy", "Tubagus", "Turki", "Turner", "Ty", "Ty-Alexander", "Tye", "Tyelor", "Tylar", "Tyler", "Tyler-James", "Tyler-Jay", "Tyllor", "Tylor", "Tymom", "Tymon", "Tymoteusz", "Tyra", "Tyree", "Tyrnan", "Tyrone", "Tyson", "Ubaid", "Ubayd", "Uchenna", "Uilleam", "Umair", "Umar", "Umer", "Umut", "Urban", "Uri", "Usman", "Uzair", "Uzayr", "Valen", "Valentin", "Valentino", "Valery", "Valo", "Vasyl", "Vedantsinh", "Veeran", "Victor", "Victory", "Vinay", "Vince", "Vincent", "Vincenzo", "Vinh", "Vinnie", "Vithujan", "Vladimir", "Vladislav", "Vrishin", "Vuyolwethu", "Wabuya", "Wai", "Walid", "Wallace", "Walter", "Waqaas", "Warkhas", "Warren", "Warrick", "Wasif", "Wayde", "Wayne", "Wei", "Wen", "Wesley", "Wesley-Scott", "Wiktor", "Wilkie", "Will", "William", "William-John", "Willum", "Wilson", "Windsor", "Wojciech", "Woyenbrakemi", "Wyatt", "Wylie", "Wynn", "Xabier", "Xander", "Xavier", "Xiao", "Xida", "Xin", "Xue", "Yadgor", "Yago", "Yahya", "Yakup", "Yang", "Yanick", "Yann", "Yannick", "Yaseen", "Yasin", "Yasir", "Yassin", "Yoji", "Yong", "Yoolgeun", "Yorgos", "Youcef", "Yousif", "Youssef", "Yu", "Yuanyu", "Yuri", "Yusef", "Yusuf", "Yves", "Zaaine", "Zaak", "Zac", "Zach", "Zachariah", "Zacharias", "Zacharie", "Zacharius", "Zachariya", "Zachary", "Zachary-Marc", "Zachery", "Zack", "Zackary", "Zaid", "Zain", "Zaine", "Zaineddine", "Zainedin", "Zak", "Zakaria", "Zakariya", "Zakary", "Zaki", "Zakir", "Zakk", "Zamaar", "Zander", "Zane", "Zarran", "Zayd", "Zayn", "Zayne", "Ze", "Zechariah", "Zeek", "Zeeshan", "Zeid", "Zein", "Zen", "Zendel", "Zenith", "Zennon", "Zeph", "Zerah", "Zhen", "Zhi", "Zhong", "Zhuo", "Zi", "Zidane", "Zijie", "Zinedine", "Zion", "Zishan", "Ziya", "Ziyaan", "Zohaib", "Zohair", "Zoubaeir", "Zubair", "Zubayr", "Zuriel"]

        self.env['equipos.coaching'].create({'name':name_team+" - Coaching Staff",'head_coach':random.choice(names),'assistant_coach':random.choice(names),'advance_scout':random.choice(names),'team':equipo})
        self.env['equipos.equipos_aux'].create({'name':name_team,'conference': equipo.conference,'city':equipo.city})
        return equipo

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'teams.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre', required=True, help='Nombre del equipo')
    conference = fields.Selection(selection=[('este', 'Este'),('oeste', 'Oeste')], string='Conferencia', default='este', required=True, help='Conferencia del equipo')
    budget = fields.Integer(string='Presupuesto',default=lambda s: random.randint(60000,90000),readonly=True)
    current_money = fields.Integer(string="Dinero restante",compute='_check_money',readonly=True)
    city = fields.Char(string='Ciudad', required=True, help='Ciudad del equipo')
    logo = fields.Image(default=_get_default_image, max_width=300, max_height=300)
    ligue = fields.Many2one('equipos.liga', ondelete='set null', help='Liga en la que juega')
    season = fields.Many2many('equipos.temporada',related='ligue.season')
    players = fields.One2many(string='Jugadores',comodel_name='equipos.jugadores',inverse_name='team')
    owner = fields.One2many(string='Dueño',comodel_name='res.partner',inverse_name='team_selected',readonly=True)
    captain = fields.Many2one('equipos.jugadores',compute='_get_captain')
    victories = fields.Integer(string='Victorias',default=0,readonly=True)
    loses = fields.Integer(string='Derrotas',default=0,readonly=True)
    draws = fields.Integer(string='Empates',default=0,readonly=True)
    coaching_staff = fields.Many2one('equipos.coaching',readonly=True)

    def _check_money(self):
        for team in self:
            team.current_money = team.budget
            for player in team.players:
                team.current_money -= float(player.pricepool)

    def _get_captain(self):
        for team in self:
            if team.players:
                team.captain = team.players[0].id
            else:
                team.captain = 0

    @api.model
    def cron_do_level(self):
        users = self.env['res.partner'].search([])
        for s in users:
            if s.ispremium:
                s.player_level+=1

    @api.model
    def cron_do_budget(self):
        users = self.env['res.partner'].search([])
        for s in users:
            if s.ispremium:
                s.team_selected.budget+=200

    @api.onchange('ligue')
    def _reset_ligue(self):
        for l in self:
            print(l.ligue.finished)
            if l.ligue.finished == 'si':
                print('Permitido')
            elif l.ligue.finished:
                raise ValidationError('No puedes añadir un equipo a una liga que está en transcurso. Para poder realizar éste cambio la liga actual y a la que quieres cambiar deben indicarse como finalizadas.')

    @api.constrains('name','city')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            if regex.match(s.city):
                print(s.city)
            else:    
                raise ValidationError('La ciudad solo acepta letras. No introduzcas números o símbolos.')

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre del equipo no se puede repetir') ]

    def cambiar_budget(self):
        for s in self:
            budget = random.randint(50000,90000)
            for p in s.players:
                budget -= p.pricepool
                if budget > 0:
                    s.write({'budget':budget})
                else:
                    raise ValidationError('El presupuesto no ha sido cambiado debido a que sería inferior al precio de los jugadores.')


    @api.onchange('name')
    def _onchange_name(self):
        return { 'warning' : {'title':'Nombre','message':'Recuerda que el nombre de cada equipo debe ser único.','type':'notification'}}

class liga(models.Model):
    _name = 'equipos.liga'
    _description = 'Liga'

    @api.model
    def create(self, values):
        ligas = super(liga, self).create(values)
        print(values)
        self.env['equipos.liga_aux'].create({'name':ligas.name})
        return ligas

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'teams.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre')
    logo = fields.Image(default=_get_default_image, max_width=100, max_height=100)
    teams = fields.One2many(string='Equipos',comodel_name='equipos.equipos',inverse_name='ligue')
    top_teams = fields.One2many(string='Equipos con mayor budget',comodel_name='equipos.equipos',inverse_name='ligue',compute='_get_top_team')
    top_winners = fields.One2many(string='Tabla de clasificación', comodel_name='equipos.equipos',inverse_name='ligue',compute='_get_winners_team')
    finished = fields.Selection(selection=[('si', 'Si'),('no', 'No')],string='Liga terminada',default='no',required=True,readonly=True)
    matches = fields.Integer(string='Partidos jugados',default=0,readonly=True)
    calendar = fields.One2many(string='Partidos',comodel_name='equipos.partidos',inverse_name='ligue')
    season = fields.Many2many(comodel_name='equipos.temporada',
                              relation='league_season',
                              column1='league_id',
                              column2='season_id')

    def renovar_season(self):
            self.write({'season' : [(4,27,0)]})

    def reset_league(self):
        cont1 = 0
        cont2 = 0
        for p in self:
            for c in p.teams:
                cont1+=1
            if cont1 > 0:
                cont2 = cont1 - 1
            else:
                cont2 = 0

            cont3 = cont1 * cont2
            if cont3 == p.matches:
                p.finished = 'si'
                p.matches = 0
                for t in p.teams:
                    t.victories = 0
                    t.loses = 0
                    t.draws = 0
                    t.owner.player_level +=1
                for i in p.calendar:
                    self.write({'calendar' : [(2,i.id,0)]})
            else:
                raise ValidationError('La temporada no ha terminado. Podrás volver a empezar cuando todos los partidos se hayan jugado (ida y vuelta)')


    def _get_top_team(self):
        for lig in self:
            if lig.teams:
                maxteam = lig.teams.filtered(lambda s: s.budget > 80000)
                lig.top_teams = maxteam.sorted(key=lambda s: s.budget, reverse=True)
            else:
                lig.top_teams = lig.teams

    def _get_winners_team(self):
        for lig in self:
            if lig.teams:
                maxteam = lig.teams.filtered(lambda s: s.victories > 0)
                lig.top_winners = maxteam.sorted(key=lambda s: s.victories, reverse=True)
            else:
                lig.top_winners = lig.teams
        
    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')

    @api.constrains('season')
    def _check_season(self):
        for s in self:
            for p in s.season:
                if p.name == str(datetime.today().year):
                    print(p.name)
                else:    
                    raise ValidationError('Se debe jugar en la temporada ' + str(datetime.today().year))

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre de la liga no se puede repetir') ]

    @api.onchange('name')
    def _onchange_name(self):
        return { 'warning' : {'title':'Nombre','message':'Recuerda que el nombre de cada liga debe ser único.','type':'notification'}}

class temporada(models.Model):
    _name = 'equipos.temporada'
    _description = 'Temporada'

    name = fields.Char(string='Temporada')
    teamsseason = fields.Many2many(comodel_name='equipos.liga',
                                   relation='league_season',
                                   column2='league_id',
                                   column1='season_id',
                                   readonly=True)    

    @api.model
    def cron_do_season(self):
        year = str(datetime.today().year)
        self.create({'name': year})

    def check_id(self):
        for l in self:
            print(l.id)
    
    @api.constrains('name')
    def _check_name(self):
        regex = re.compile('^(20[2-9]\d|2[1-9]\d{2}|[3-9]\d{3}|[1-9]\d{4,})$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('La temporada solo acepta a partir del año 2020 en el siguiente formato -> 2021')

    _sql_constraints = [ ('name_uniq','unique(name)','La temporada debe ser única') ]

class jugadores(models.Model):
    _name = 'equipos.jugadores'
    _description = 'Jugadores'

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'player_silhouette.jpg'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    name = fields.Char(string='Nombre',required=True)
    logo = fields.Image(default=_get_default_image, max_width=300, max_height=300)
    position = fields.Selection(selection=[('base', 'PG'),('escolta', 'SG'),('alero', 'SF'),('alapivot', 'PF'),('pivot', 'C')], string='Posicion', default='base', required=True, help='Posicion del jugador')
    nationality = fields.Char(string='Nacionalidad')
    team = fields.Many2one('equipos.equipos', ondelete='set null')
    free = fields.Selection(selection=[('si', 'Si'),('no', 'No')], string='Permitir su venta', default='no', required=True)
    pricepool = fields.Integer(default=lambda s: random.randint(2000,8000),readonly=True)

    @api.constrains('name','nationality')
    def _check_name(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        for s in self:
            if regex.match(s.name):
                print(s.name)
            else:    
                raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            if regex.match(s.nationality):
                print(s.nationality)
            else:    
                raise ValidationError('La nacionalidad solo acepta letras. No introduzcas números o símbolos.')

    @api.constrains('team','pricepool','free')
    def _check_money(self):
        for s in self:
            print("team2 current_money - pricepool: " + str(s.team.current_money - s.pricepool))
            if s.free == 'si' and (s.team.current_money - s.pricepool) > 0:
                print(s.team.budget - s.pricepool)
            else:    
                raise ValidationError('El equipo no dispone de dinero suficiente para realizar el fichaje o el jugador no está a la venta. Lo sentimos.')

    _sql_constraints = [ ('name_uniq','unique(name)','El nombre completo del jugador no se puede repetir') ]            

class partidos(models.Model):
    _name = 'equipos.partidos'
    _description = 'Partidos'

    @api.model
    def create(self, values):
        partido = super(partidos, self).create(values)
        print(values)
        for i in partido:
            if i.team1_points > i.team2_points:
                i.winner = i.team1.name
                i.team1.owner.player_level +=1
                if i.team1.owner.player_level > 1 and i.team1.owner.ispremium == True:
                    i.team1.captain.free = 'si'
                    i.team1.captain.pricepool = 0
                    print("team1")

                i.team1.victories +=1
                i.team2.loses +=1
                i.ligue.matches +=1
            elif i.team2_points > i.team1_points:
                i.winner = i.team2.name
                i.team2.owner.player_level +=1
                if i.team2.owner.player_level > 1 and i.team2.owner.ispremium == True:
                    i.team2.captain.free = 'si'
                    i.team2.captain.pricepool = 0

                i.team2.victories +=1
                i.team1.loses +=1
                i.ligue.matches +=1
            else:
                i.winner = 'Empate'
                i.team1.draws += 1
                i.team2.draws += 1
                i.ligue.matches +=1
        
        return partido

    name = fields.Char(string='', compute='_get_name')
    date = fields.Datetime(string='Fecha',required=True)
    hours = fields.Integer(string='Duración del partido en horas',default=lambda s: random.randint(1,2),required=True,readonly=True)
    ligue = fields.Many2one('equipos.liga', required=True)
    team1 = fields.Many2one('equipos.equipos', string='Local',required=True)
    team2 = fields.Many2one('equipos.equipos', string='Visitante',required=True)
    team1_points = fields.Integer(string='Puntos local',default=lambda s: random.randint(80,120),readonly=True)
    team2_points = fields.Integer(string='Puntos visitante',default=lambda s: random.randint(80,120),readonly=True)
    result = fields.Char(string='Resultado',compute='_get_result',readonly=True)
    winner = fields.Char(string='Ganador',readonly=True)

    def _get_result(self):
        for i in self:
            i.result = str(i.team1.name) + ' ' + str(i.team1_points) + " - " + str(i.team2.name) + ' ' + str(i.team2_points)

    def _get_name(self):
        for i in self:
            i.name = str(i.team1.name).upper() + " - " + str(i.team2.name).upper()
        
    @api.constrains('name','ligue')
    def _get_matches(self):
        all_matches = self.env['equipos.partidos'].search([])
        all_match = all_matches[:-1]

        for p in all_match:
            for i in self:
                if str(p.name) == str(i.name) and str(i.ligue.name) == str(p.ligue.name):
                    raise ValidationError('Este partido ya ha sido jugado.')
                else:    
                    for p in i.ligue:
                        if p.finished == 'si':
                            p.finished = 'no'
            
    @api.constrains('team1','team2')
    def _check_teams(self):
        for s in self:
            if s.team1.name == s.team2.name:
                raise ValidationError('Los equipos deben ser distintos para poder jugar el partido.')
            else:    
                print('Movimiento correcto')

    @api.constrains('team1','team2','ligue')
    def _check_ligue(self):
        for s in self:
            if s.team1 not in s.ligue.teams:
                raise ValidationError(s.team1.name + ' no forma parte de la liga ' + s.ligue.name) 
            else:    
                print('Movimiento correcto')
            if s.team2 not in s.ligue.teams:
                raise ValidationError(s.team2.name + ' no forma parte de la liga ' + s.ligue.name) 
            else:    
                print('Movimiento correcto')

class coaching(models.Model):
    _name = 'equipos.coaching'
    _description = 'Cuerpo técnico'

    name = fields.Char(string='')
    head_coach = fields.Char(string='Head coach')
    assistant_coach = fields.Char(string='Assistant coach')
    advance_scout = fields.Char(string='Advance scout')
    team = fields.One2many(string='Equipo',comodel_name='equipos.equipos',inverse_name='coaching_staff')

class users(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    nickname = fields.Char(string='Nickname')
    team_selected = fields.Many2one('equipos.equipos', string='Mi equipo')
    player_level = fields.Integer(string='Nivel de experiencia', default=0,readonly=True)
    isuser = fields.Boolean(string="Usuario",default=True)
    ispremium = fields.Boolean(string="Usuario premium",default=False)

    @api.onchange('team_selected')
    def _check_team(self):
        teams = self.env['res.partner'].search([])
        all_teams = teams.team_selected[:-1]
        for p in all_teams:
            for s in self:
                if str(s.team_selected) == str(p):
                    raise ValidationError(s.team_selected.name + ' ya tiene dueño.') 
                else:    
                    print('Movimiento correcto')

class userspremium(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def _get_default_image(self):
        with open(modules.get_module_resource('equipos', 'static/src/img', 'premium_logo.png'), 'rb') as f:
            img = f.read()
            return base64.b64encode(img)

    premium_logo = fields.Image(default=_get_default_image, max_width=300, max_height=300)
    boost_budget = fields.Char(string='Boost de budget',default='Se añadirán 200 créditos al budget del equipo diariamente.',readonly=True)
    boost_level = fields.Char(string='Boost de nivel: ',default='Se subirá 1 nivel a la cuenta semanalmente.',readonly=True)
    premium_players = fields.Char(string='Jugador gratuito: ',default='Cuando la cuenta alcanze el nivel 10 el capitán del equipo pasará a ser gratuito.',readonly=True)
    premium_logo = fields.Image(default=_get_default_image, max_width=100, max_height=100)

class partidos_wizard(models.TransientModel):
    _name = 'equipos.partidos_wizard'
    state = fields.Selection([('1','Fecha'),('2','Liga'),('3','Equipos'),('4','Crear')],default='1')
    name = fields.Char(string='Partido',readonly=True)
    date = fields.Datetime(string='Fecha')
    ligue = fields.Many2one('equipos.liga_aux')
    l_name = fields.Char(string='Nombre liga')
    team1 = fields.Many2one('equipos.equipos_aux', string='Local')
    team2 = fields.Many2one('equipos.equipos_aux', string='Visitante')
    t1_name = fields.Char(string="Nombre equipo local")
    t2_name = fields.Char(string="Nombre equipo visitante")
    t1_conference = fields.Selection(selection=[('este', 'Este'),('oeste', 'Oeste')], string='Conferencia', default='este', help='Conferencia del equipo')
    t2_conference = fields.Selection(selection=[('este', 'Este'),('oeste', 'Oeste')], string='Conferencia', default='este', help='Conferencia del equipo')
    t1_city = fields.Char(string='Ciudad', help='Ciudad del equipo')
    t2_city = fields.Char(string='Ciudad', help='Ciudad del equipo')

    @api.model
    def action_partido_wizard(self):
        action = self.env.ref('equipos.action_partido_wizard').read()[0]
        return action

    def next(self):
        if self.state == '1':
            self.state = '2'
        elif self.state == '2':
            self.state = '3'
        elif self.state == '3':
            self.state = '4'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
    
    def previous(self):
        if self.state == '2':
            self.state = '1'
        elif self.state == '3':
            self.state = '2'
        elif self.state == '4':
            self.state = '3'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def add_ligue(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        ligas = self.env['equipos.liga'].search([])
        ligas_aux = self.env['equipos.liga_aux'].search([])
        for p in ligas:
            if p.name == self.l_name:
                raise ValidationError('Ésta liga ya existe.')
        for p in ligas_aux:
            if p.name == self.l_name:
                raise ValidationError('Ésta liga ya existe.')

        for c in self:
            #c.write({'ligue':[(0,0,{'name':c.l_name})]})
            if c.l_name != False:
                if regex.match(c.l_name):
                    c.env['equipos.liga_aux'].create({'name': c.l_name})
                else:
                    raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            else:
                raise ValidationError('El nombre de la liga no puede estar vacío.')

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def add_team(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        equipos = self.env['equipos.equipos'].search([])
        equipos_aux = self.env['equipos.equipos_aux'].search([])
        liga = self.env['equipos.liga_aux'].search([])
        li = self.env['equipos.liga_aux']
        for p in equipos:
            if p.name == self.t1_name:
                raise ValidationError('El equipo local ya existe.')
            if p.name == self.t2_name:
                raise ValidationError('El equipo visitante ya existe.')
        for p in equipos_aux:
            if p.name == self.t1_name:
                raise ValidationError('El equipo local ya existe.')
            if p.name == self.t2_name:
                raise ValidationError('El equipo visitante ya existe.')

        for c in self:
            if c.t1_name != False:
                if regex.match(c.t1_name):
                    c.env['equipos.equipos_aux'].create({'name': c.t1_name,'conference': c.t1_conference,'city': c.t1_city,'ligue': c.ligue.id})
                else:
                    raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            else:
                raise ValidationError('El nombre del equipo local no puede estar vacío.')
            if c.t2_name != False:
                if regex.match(c.t2_name):
                    c.env['equipos.equipos_aux'].create({'name': c.t2_name,'conference': c.t2_conference,'city': c.t2_city,'ligue': c.ligue.id})
                else:
                    raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            else:
                raise ValidationError('El nombre del equipo visitante no puede estar vacío.')

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
    
    def add_local(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        equipos = self.env['equipos.equipos'].search([])
        equipos_aux = self.env['equipos.equipos_aux'].search([])
        liga = self.env['equipos.liga_aux'].search([])
        li = self.env['equipos.liga_aux']
        for p in equipos:
            if p.name == self.t1_name:
                raise ValidationError('El equipo local ya existe.')
        for p in equipos_aux:
            if p.name == self.t1_name:
                raise ValidationError('El equipo local ya existe.')

        for c in self:
            if c.t1_name != False:
                if regex.match(c.t1_name):
                    c.env['equipos.equipos_aux'].create({'name': c.t1_name,'conference': c.t1_conference,'city': c.t1_city,'ligue': c.ligue.id})
                else:
                    raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            else:
                raise ValidationError('El nombre del equipo local no puede estar vacío.')

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def add_visitante(self):
        regex = re.compile('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',re.I)
        equipos = self.env['equipos.equipos'].search([])
        equipos_aux = self.env['equipos.equipos_aux'].search([])
        liga = self.env['equipos.liga_aux'].search([])
        li = self.env['equipos.liga_aux']
        for p in equipos:
            if p.name == self.t2_name:
                raise ValidationError('El equipo local ya existe.')
        for p in equipos_aux:
            if p.name == self.t2_name:
                raise ValidationError('El equipo local ya existe.')

        for c in self:
            if c.t2_name != False:
                if regex.match(c.t2_name):
                    c.env['equipos.equipos_aux'].create({'name': c.t2_name,'conference': c.t2_conference,'city': c.t2_city,'ligue': c.ligue.id})
                else:
                    raise ValidationError('El nombre solo acepta letras. No introduzcas números o símbolos.')
            else:
                raise ValidationError('El nombre del equipo visitanteno puede estar vacío.')

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    #def commit(self):
    #    return {
    #        'type': 'ir.actions.act_window',
    #        'res_model': self._name,
    #        'res_id': self.id,
    #        'view_mode': 'form',
    #        'target': 'new',
    #    }

    def create_partido(self):
        for c in self:
            nombre = str(c.t1_name).upper() + " - " + str(c.t2_name).upper()
            #ligue = c.env['equipos.liga'].create({'name':c.l_name,'finished':'si','date':c.date})
            #team1: c.env['equipos.equipos'].create({'name':c.t1_name,'conference':c.t1_conference,'city':c.t1_city,'ligue':ligue})
            liga = c.env['equipos.liga'].search([])
            teams = []
            entra = False
            entra2 = False
            entra3 = False
            #partido = c.env['equipos.partidos']
        for cl in c.ligue:
            liga = c.env['equipos.liga'].search([])
            for l in liga:
                if cl.name == l.name:
                    entra = True
                    ligue = l
            if entra == False:
                ligue = c.env['equipos.liga'].create({'name':cl.name,'finished':'si'})
        for st in c.team1:
            equipo = c.env['equipos.equipos'].search([])
            for t in equipo:
                if st.name == t.name:
                    entra2 = True
                    team1 = t
            if entra2 == False:
                team1=c.env['equipos.equipos'].create({'name': st.name,
                                                    'conference': st.conference,
                                                    'city': st.city,
                                                    'ligue': ligue.id
                                                    })
        for ts in c.team2:
            equipo = c.env['equipos.equipos'].search([])
            for tp in equipo:
                if ts.name == tp.name:
                    entra3 = True
                    team2 = tp
            if entra3 == False:
                team2=c.env['equipos.equipos'].create({'name': ts.name,
                                                    'conference': ts.conference,
                                                    'city': ts.city,
                                                    'ligue': ligue.id
                                                    })
        partido = c.env['equipos.partidos'].create({'name': nombre,'date':c.date,'ligue':ligue.id,'team1':team1.id,'team2':team2.id})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'equipos.partidos',
            'res_id': partido.id,
            'view_mode': 'form',
            'target': 'current',
    	}

class ligue_aux(models.TransientModel):
    _name = 'equipos.liga_aux'

    ligue_original = fields.Many2one('equipos.liga')
    name = fields.Char(string='Nombre')
    #partidos = fields.One2many(comodel_name='equipos.partidos_wizard',inverse_name='ligue')
    teams = fields.One2many(string='Equipos',comodel_name='equipos.equipos_aux',inverse_name='ligue')
    #calendar = fields.One2many(string='Partidos',comodel_name='equipos.partidos_wizard',inverse_name='ligue')

class equipos_aux(models.TransientModel):
    _name = 'equipos.equipos_aux'

    teams_original = fields.Many2one('equipos.equipos')
    name = fields.Char(string='Nombre')
    conference = fields.Selection(selection=[('este', 'Este'),('oeste', 'Oeste')], string='Conferencia', help='Conferencia del equipo')
    city = fields.Char(string='Ciudad', help='Ciudad del equipo')
    ligue = fields.Many2one('equipos.liga_aux')

class jugador_wizard(models.TransientModel):
    _name = 'equipos.jugador_wizard'

    name = fields.Char(string='Nombre',required=True)
    logo = fields.Image(max_width=300, max_height=300)
    position = fields.Selection(selection=[('base', 'PG'),('escolta', 'SG'),('alero', 'SF'),('alapivot', 'PF'),('pivot', 'C')], string='Posicion', default='base', help='Posicion del jugador')
    nationality = fields.Char(string='Nacionalidad')

    @api.model
    def action_jugador_wizard(self):
        print('tomatito')
        action = self.env.ref('equipos.action_jugador_wizard').read()[0]
        return action

    def create_jugador(self):
        equipo = self.env.context.get('equipo_id')
        print(equipo)
        for c in self:
            jugador = c.env['equipos.jugadores'].create({'name': c.name,'logo':c.logo,'position':c.position,'nationality':c.nationality,'team':equipo,'free':'si'})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'equipos.jugadores',
            'res_id': jugador.id,
            'view_mode': 'form',
            'target': 'current',
    	}