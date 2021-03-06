import re
import dropbox

district = {
    1:"1-Srikakulam",
    2:"1-Srikakulam",
    3:"1-Srikakulam",
    4:"1-Srikakulam",
    5:"1-Srikakulam",
    6:"1-Srikakulam",
    7:"1-Srikakulam",
    8:"1-Srikakulam",
    9:"1-Srikakulam",
    10:"1-Srikakulam",
    11:"2-Vizianagaram",
    12:"2-Vizianagaram",
    13:"2-Vizianagaram",
    14:"2-Vizianagaram",
    15:"2-Vizianagaram",
    16:"2-Vizianagaram",
    17:"2-Vizianagaram",
    18:"2-Vizianagaram",
    19:"2-Vizianagaram",
    20:"3-Visakhapatnam",
    21:"3-Visakhapatnam",
    22:"3-Visakhapatnam",
    23:"3-Visakhapatnam",
    24:"3-Visakhapatnam",
    25:"3-Visakhapatnam",
    26:"3-Visakhapatnam",
    27:"3-Visakhapatnam",
    28:"3-Visakhapatnam",
    29:"3-Visakhapatnam",
    30:"3-Visakhapatnam",
    31:"3-Visakhapatnam",
    32:"3-Visakhapatnam",
    33:"3-Visakhapatnam",
    34:"3-Visakhapatnam",
    35:"4-East Godavari",
    36:"4-East Godavari",
    37:"4-East Godavari",
    38:"4-East Godavari",
    39:"4-East Godavari",
    40:"4-East Godavari",
    41:"4-East Godavari",
    42:"4-East Godavari",
    43:"4-East Godavari",
    44:"4-East Godavari",
    45:"4-East Godavari",
    46:"4-East Godavari",
    47:"4-East Godavari",
    48:"4-East Godavari",
    49:"4-East Godavari",
    50:"4-East Godavari",
    51:"4-East Godavari",
    52:"4-East Godavari",
    53:"4-East Godavari",
    54:"5-West Godavari",
    55:"5-West Godavari",
    56:"5-West Godavari",
    57:"5-West Godavari",
    58:"5-West Godavari",
    59:"5-West Godavari",
    60:"5-West Godavari",
    61:"5-West Godavari",
    62:"5-West Godavari",
    63:"5-West Godavari",
    64:"5-West Godavari",
    65:"5-West Godavari",
    66:"5-West Godavari",
    67:"5-West Godavari",
    68:"5-West Godavari",
    69:"6-Krishna",
    70:"6-Krishna",
    71:"6-Krishna",
    72:"6-Krishna",
    73:"6-Krishna",
    74:"6-Krishna",
    75:"6-Krishna",
    76:"6-Krishna",
    77:"6-Krishna",
    78:"6-Krishna",
    79:"6-Krishna",
    80:"6-Krishna",
    81:"6-Krishna",
    82:"6-Krishna",
    83:"6-Krishna",
    84:"6-Krishna",
    85:"7-Guntur",
    86:"7-Guntur",
    87:"7-Guntur",
    88:"7-Guntur",
    89:"7-Guntur",
    90:"7-Guntur",
    91:"7-Guntur",
    92:"7-Guntur",
    93:"7-Guntur",
    94:"7-Guntur",
    95:"7-Guntur",
    96:"7-Guntur",
    97:"7-Guntur",
    98:"7-Guntur",
    99:"7-Guntur",
    100:"7-Guntur",
    101:"7-Guntur",
	102:"8-Prakasam",
	103:"8-Prakasam",
	104:"8-Prakasam",
	105:"8-Prakasam",
	106:"8-Prakasam",
	107:"8-Prakasam",
	108:"8-Prakasam",
	109:"8-Prakasam",
	110:"8-Prakasam",
	111:"8-Prakasam",
	112:"8-Prakasam",
	113:"8-Prakasam",
    114:"9-Nellore",
    115:"9-Nellore",
    116:"9-Nellore",
    117:"9-Nellore",
    118:"9-Nellore",
    119:"9-Nellore",
    120:"9-Nellore",
    121:"9-Nellore",
    122:"9-Nellore",
    123:"9-Nellore",
    124:"10-Kadapa",
    125:"10-Kadapa",
    126:"10-Kadapa",
    127:"10-Kadapa",
    128:"10-Kadapa",
    129:"10-Kadapa",
    130:"10-Kadapa",
    131:"10-Kadapa",
    132:"10-Kadapa",
    133:"10-Kadapa",
    134:"11-Kurnool",
    135:"11-Kurnool",
    136:"11-Kurnool",
    137:"11-Kurnool",
    138:"11-Kurnool",
    139:"11-Kurnool",
    140:"11-Kurnool",
    141:"11-Kurnool",
    142:"11-Kurnool",
    143:"11-Kurnool",
    144:"11-Kurnool",
    145:"11-Kurnool",
    146:"11-Kurnool",
    147:"11-Kurnool",
    148:"12-Anantapur",
    149:"12-Anantapur",
    150:"12-Anantapur",
    151:"12-Anantapur",
    152:"12-Anantapur",
    153:"12-Anantapur",
    154:"12-Anantapur",
    155:"12-Anantapur",
    156:"12-Anantapur",
    157:"12-Anantapur",
    158:"12-Anantapur",
    159:"12-Anantapur",
    160:"12-Anantapur",
    161:"12-Anantapur",
    162:"13-Chittoor",
    163:"13-Chittoor",
    164:"13-Chittoor",
    165:"13-Chittoor",
    166:"13-Chittoor",
    167:"13-Chittoor",
    168:"13-Chittoor",
    169:"13-Chittoor",
    170:"13-Chittoor",
    171:"13-Chittoor",
    172:"13-Chittoor",
    173:"13-Chittoor",
    174:"13-Chittoor",
    175:"13-Chittoor"
}

const = {
    1:"1-Ichchapuram",
    2:"2-Palasa",
    3:"3-Tekkali",
    4:"4-Pathapatnam",
    5:"5-Srikakulam",
    6:"6-Amadalavalasa",
    7:"7-Etcherla",
    8:"8-Narasannapeta",
    9:"9-Rajam (SC)",
    10:"10-Palakonda (ST)",
    11:"11-Kurupam (ST)",
    12:"12-Parvathipuram (SC)",
    13:"13-Salur (ST)",
    14:"14-Bobbili",
    15:"15-Cheepurupalle",
    16:"16-Gajapathinagaram",
    17:"17-Nellimarla",
    18:"18-Vizianagaram",
    19:"19-Srungavarapukota",
    20:"20-Bhimili",
    21:"21-Visakhapatnam East",
    22:"22-Visakhapatnam South",
    23:"23-Visakhapatnam North",
    24:"24-Visakhapatnam West",
    25:"25-Gajuwaka",
    26:"26-Chodavaram",
    27:"27-Madugula",
    28:"28-Araku Valley (ST)",
    29:"29-Paderu (ST)",
    30:"30-Anakapalle",
    31:"31-Pendurthi",
    32:"32-Yelamanchili",
    33:"33-Payakaraopet (SC)",
    34:"34-Narsipatnam",
    35:"35-Tuni",
    36:"36-Prathipadu",
    37:"37-Pithapuram",
    38:"38-Kakinada Rural",
    39:"39-Peddapuram",
    40:"40-Anaparthy",
    41:"41-Kakinada City",
    42:"42-Ramachandrapuram",
    43:"43-Mummidivaram",
    44:"44-Amalapuram (SC)",
    45:"45-Razole (SC)",
    46:"46-Gannavaram (SC)",
    47:"47-Kothapeta",
    48:"48-Mandapeta",
    49:"49-Rajanagaram",
    50:"50-Rajahmundry City",
    51:"51-Rajahmundry Rural",
    52:"52-Jaggampeta",
    53:"53-Rampachodavaram (ST)",
    54:"54-Kovvur (SC)",
    55:"55-Nidadavole",
    56:"56-Achanta",
    57:"57-Palacole",
    58:"58-Narasapuram",
    59:"59-Bhimavaram",
    60:"60-Undi",
    61:"61-Tanuku",
    62:"62-Tadepalligudem",
    63:"63-Ungutur",
    64:"64-Denduluru",
    65:"65-Eluru",
    66:"66-Gopalapuram (SC)",
    67:"67-Polavaram (ST)",
    68:"68-Chintalapudi (SC)",
    69:"69-Tiruvuru (SC)",
    70:"70-Nuzvid",
    71:"71-Gannavaram",
    72:"72-Gudivada",
    73:"73-Kaikalur",
    74:"74-Pedana",
    75:"75-Machilipatnam",
    76:"76-Avanigadda",
    77:"77-Pamarru (SC)",
    78:"78-Penamaluru",
    79:"79-Vijayawada West",
    80:"80-Vijayawada Central",
    81:"81-Vijayawada East",
    82:"82-Mylavaram",
    83:"83-Nandigama (SC)",
    84:"84-Jaggayyapeta",
    85:"85-Pedakurapadu",
    86:"86-Tadikonda (SC)",
    87:"87-Mangalagiri",
    88:"88-Ponnur",
    89:"89-Vemuru (SC)",
    90:"90-Repalle",
    91:"91-Tenali",
    92:"92-Bapatla",
    93:"93-Prathipadu (SC)",
    94:"94-Guntur West",
    95:"95-Guntur East",
    96:"96-Chilakaluripet",
    97:"97-Narasaraopet",
    98:"98-Sattenapalle",
    99:"99-Vinukonda",
    100:"100-Gurajala",
    101:"101-Macherla",
    102:"102-Yerragondapalem (SC)",
    103:"103-Darsi",
    104:"104-Parchur",
    105:"105-Addanki",
    106:"106-Chirala",
    107:"107-Santhanuthalapadu (SC)",
    108:"108-Ongole",
    109:"109-Kandukur",
    110:"110-Kondapi (SC)",
    111:"111-Markapuram",
    112:"112-Giddalur",
    113:"113-Kanigiri",
    114:"114-Kavali",
    115:"115-Atmakur",
    116:"116-Kovur",
    117:"117-Nellore City",
    118:"118-Nellore Rural",
    119:"119-Sarvepalli",
    120:"120-Gudur (SC)",
    121:"121-Sullurpeta (SC)",
    122:"122-Venkatagiri",
    123:"123-Udayagiri",
    124:"124-Badvel (SC)",
    125:"125-Rajampet",
    126:"126-Kadapa",
    127:"127-Kodur (SC)",
    128:"128-Rayachoti",
    129:"129-Pulivendla",
    130:"130-Kamalapuram",
    131:"131-Jammalamadugu",
    132:"132-Proddatur",
    133:"133-Mydukur",
    134:"134-Allagadda",
    135:"135-Srisailam",
    136:"136-Nandikotkur (SC)",
    137:"137-Kurnool",
    138:"138-Panyam",
    139:"139-Nandyal",
    140:"140-Banaganapalle",
    141:"141-Dhone",
    142:"142-Pattikonda",
    143:"143-Kodumur (SC)",
    144:"144-Yemmiganur",
    145:"145-Mantralayam",
    146:"146-Adoni",
    147:"147-Alur",
    148:"148-Rayadurg",
    149:"149-Uravakonda",
    150:"150-Guntakal",
    151:"151-Tadpatri",
    152:"152-Singanamala (SC)",
    153:"153-Anantapur Urban",
    154:"154-Kalyandurg",
    155:"155-Raptadu",
    156:"156-Madakasira (SC)",
    157:"157-Hindupur",
    158:"158-Penukonda",
    159:"159-Puttaparthi",
    160:"160-Dharmavaram",
    161:"161-Kadiri",
    162:"162-Thamballapalle",
    163:"163-Pileru",
    164:"164-Madanapalle",
    165:"165-Punganur",
    166:"166-Chandragiri",
    167:"167-Tirupati",
    168:"168-Srikalahasti",
    169:"169-Satyavedu (SC)",
    170:"170-Nagari",
    171:"171-Gangadhara Nellore (SC)",
    172:"172-Chittoor",
    173:"173-Puthalapattu (SC)",
    174:"174-Palamaner",
    175:"175-Kuppam"
}

dbx = dropbox.Dropbox(
    "O8tHMaacfEAAAAAAAAAAeyMCLUL1cNBTesZVLBIKTpP8AQ1_WdYbYEe_We4P63UA"
)

DROPBOX_INPUT_PATH = "/1-Srikakulam/"

response = dbx.files_list_folder(path=DROPBOX_INPUT_PATH, recursive=True)

for entry in response.entries:
    r = re.match('S01A(\d\d\d)P(\d\d\d).PDF', entry.name)
    if r:
        d = r.group(1).lstrip("0")
        c = r.group(2).lstrip("0")
        do = district[int(d)]
        co = const[int(d)]
        from_path = entry.path_display
        to_path = "/DATA/{}/{}/{}".format(do, co, entry.name)
        try:
            dbx.files_get_metadata(to_path)
        except Exception as e:
            print("Copying file From: {} To: {}".format(from_path,
                                                        to_path))
            try:
                dbx.files_move(from_path, to_path)
                #dbx.files_delete(from_path)
            except Exception as e:
                print("File copy failed for {}".format(str(e)))
        else:
            print("File already exists {}. File deleted.".format(
                from_path))
            dbx.files_delete(from_path)
