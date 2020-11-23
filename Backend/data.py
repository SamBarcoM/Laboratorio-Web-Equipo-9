#Información aleatoria de http://www.generatedata.com/ para poblar la base de datos de estudiantes

# Classes
from mongo_functions import mongoController


students = [
	{
		"name": "Leilani Dunn",
		"phone": "+5216677994804",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a02821688",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Randall Mercado",
		"phone": "+5215270166809",
		"campus": "CEM",
		"career": "LEF",
		"student_number": "a03907721",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Brenden Bush",
		"phone": "+5213960961836",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a04507949",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Cameran Howell",
		"phone": "+5215522003033",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a06937546",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Quinn Nielsen",
		"phone": "+5213302742845",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a06598820",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Gregory Drake",
		"phone": "+5216083542983",
		"campus": "CEM",
		"career": "ITC",
		"student_number": "a05889526",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Brenda Stout",
		"phone": "+5217712765669",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a08574650",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Aurora Clarke",
		"phone": "+5217401426416",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a08409591",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Olivia Prince",
		"phone": "+5218507189970",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a06585356",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Nomlanga Sweeney",
		"phone": "+5214776817314",
		"campus": "CCM",
		"career": "LIN",
		"student_number": "a08712079",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Amal Webster",
		"phone": "+5211102644059",
		"campus": "CCM",
		"career": "ITC",
		"student_number": "a02782224",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Ray Prince",
		"phone": "+5215368672554",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a06876850",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Fatima Sawyer",
		"phone": "+5211022557728",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a09689971",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Wylie Fisher",
		"phone": "+5213934224805",
		"campus": "CEM",
		"career": "LEF",
		"student_number": "a03227221",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Amity Blevins",
		"phone": "+5218486897469",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a09369857",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Maya Guy",
		"phone": "+5219934569876",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a00299675",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Kitra Bentley",
		"phone": "+5218117372871",
		"campus": "CSF",
		"career": "LIN",
		"student_number": "a08646214",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Orlando Whitney",
		"phone": "+5215181182557",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a04767572",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Cora Griffith",
		"phone": "+5219821780156",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a07577891",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Gavin Cardenas",
		"phone": "+5216113180203",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a07646824",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Herman Strong",
		"phone": "+5210241741902",
		"campus": "CEM",
		"career": "ITC",
		"student_number": "a07544529",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Brian Huffman",
		"phone": "+5217508166392",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a09310388",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Sonya Lang",
		"phone": "+5214181144654",
		"campus": "CEM",
		"career": "LEF",
		"student_number": "a02244154",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Ian Williamson",
		"phone": "+5215720233765",
		"campus": "CEM",
		"career": "LEF",
		"student_number": "a00681041",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Vivien Romero",
		"phone": "+5214223921867",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a07229615",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Signe Pitts",
		"phone": "+5211553081348",
		"campus": "CSF",
		"career": "LIN",
		"student_number": "a02112049",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Louis Mccray",
		"phone": "+5215275690941",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a02141879",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Neville Wilson",
		"phone": "+5214973042378",
		"campus": "CCM",
		"career": "LIN",
		"student_number": "a06246303",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Yuli Burns",
		"phone": "+5212520600087",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a06098159",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Sage Gregory",
		"phone": "+5216679196989",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a06766978",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Ian Ramsey",
		"phone": "+5214985083446",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a07939385",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Upton Bennett",
		"phone": "+5216191721254",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a01900602",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Brynn Lester",
		"phone": "+5217282189649",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a08062868",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Karina Sampson",
		"phone": "+5213028788641",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a01180612",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Karly Mcclain",
		"phone": "+5215867062638",
		"campus": "CSF",
		"career": "IDS",
		"student_number": "a07458555",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Noble Ramsey",
		"phone": "+5212733805186",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a09249495",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Valentine Tyson",
		"phone": "+5216434706171",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a05565990",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Galvin Humphrey",
		"phone": "+5211446062246",
		"campus": "CCM",
		"career": "IMT",
		"student_number": "a02503457",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Mason Bird",
		"phone": "+5213762271341",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a07541746",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Fredericka Ortiz",
		"phone": "+5214376778605",
		"campus": "CEM",
		"career": "ITC",
		"student_number": "a01282715",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Malik Cannon",
		"phone": "+5216559779632",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a09212916",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Quentin Chase",
		"phone": "+5214110951262",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a09410983",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Ivy Holcomb",
		"phone": "+5214065756941",
		"campus": "CCM",
		"career": "LAF",
		"student_number": "a02227711",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Ifeoma Bird",
		"phone": "+5213560739966",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a07525995",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Kimberley Suarez",
		"phone": "+5215916588030",
		"campus": "CCM",
		"career": "IMT",
		"student_number": "a09299041",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Kyla Sheppard",
		"phone": "+5210856215757",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a09613452",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Giselle Gilmore",
		"phone": "+5213475687976",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a05283516",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Quentin Norman",
		"phone": "+5218829635441",
		"campus": "CCM",
		"career": "LIN",
		"student_number": "a09176632",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Ria Cooley",
		"phone": "+5216865691687",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a07210018",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Idola Ferguson",
		"phone": "+5213355669543",
		"campus": "CCM",
		"career": "LIN",
		"student_number": "a00663235",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Wade Duke",
		"phone": "+5212689111678",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a08498568",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Ariel Glover",
		"phone": "+5214384008955",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a07677143",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Tate Zimmerman",
		"phone": "+5216170699176",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a03393848",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Jolene Castro",
		"phone": "+5217697133629",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a07254400",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Allegra Bush",
		"phone": "+5217641818394",
		"campus": "CSF",
		"career": "LIN",
		"student_number": "a00460544",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Lacey Patel",
		"phone": "+5215110429276",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a09561496",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Zoe Hickman",
		"phone": "+5211870054992",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a08322053",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Reece Francis",
		"phone": "+5217002921080",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a08241384",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Adrienne Higgins",
		"phone": "+5216214752191",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a02556460",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Clio Roman",
		"phone": "+5213401930011",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a04916028",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Lee Long",
		"phone": "+5216008025741",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a05759295",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Maia Cannon",
		"phone": "+5211832765658",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a05250488",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Alfonso Sherman",
		"phone": "+5214646634658",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a02992153",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Oprah Clemons",
		"phone": "+5218406268097",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a09370432",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Jael Forbes",
		"phone": "+5214538298598",
		"campus": "CCM",
		"career": "LAF",
		"student_number": "a01253530",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Xandra Dunn",
		"phone": "+5213103636085",
		"campus": "CSF",
		"career": "IDS",
		"student_number": "a06589780",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Jaime Delaney",
		"phone": "+5218397310110",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a08552205",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Sopoline Harmon",
		"phone": "+5212430499495",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a00731660",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Griffith Barry",
		"phone": "+5216829783417",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a09879676",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Jenna Brock",
		"phone": "+5216133692259",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a02652424",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Veronica Cobb",
		"phone": "+5216604466906",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a08485302",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Noelle Barber",
		"phone": "+5216075175304",
		"campus": "CCM",
		"career": "IMT",
		"student_number": "a02390585",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Audra Powell",
		"phone": "+5216304548304",
		"campus": "CCM",
		"career": "LAF",
		"student_number": "a01758474",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Rooney Johns",
		"phone": "+5214177865629",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a02657570",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Nathaniel Guy",
		"phone": "+5212479975611",
		"campus": "CEM",
		"career": "IMT",
		"student_number": "a05162395",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Claudia Wolf",
		"phone": "+5213837678269",
		"campus": "CCM",
		"career": "ITC",
		"student_number": "a01302547",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Ayanna Washington",
		"phone": "+5218856337609",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a03863959",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Whilemina York",
		"phone": "+5214736474071",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a06977279",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Zelenia Witt",
		"phone": "+5218837079655",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a07502604",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Lunea Carson",
		"phone": "+5215029817155",
		"campus": "CEM",
		"career": "LIN",
		"student_number": "a08576403",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Elaine Guerra",
		"phone": "+5214417116948",
		"campus": "CSF",
		"career": "ITC",
		"student_number": "a02875740",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Odette Dunn",
		"phone": "+5210926947790",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a00268190",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Dara Moody",
		"phone": "+5212344912683",
		"campus": "CCM",
		"career": "ITC",
		"student_number": "a09621037",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Gisela Holden",
		"phone": "+5217893174459",
		"campus": "CCM",
		"career": "LAF",
		"student_number": "a05589443",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Christine Booth",
		"phone": "+5212496958871",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a03171575",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Nathaniel Fitzpatrick",
		"phone": "+5216349553888",
		"campus": "CEM",
		"career": "ITC",
		"student_number": "a06082997",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Griffith Hoover",
		"phone": "+5215744932164",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a01516323",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Grace Jensen",
		"phone": "+5210326696466",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a08962389",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Lila Hanson",
		"phone": "+5211449239690",
		"campus": "CSF",
		"career": "LAF",
		"student_number": "a04672835",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Benedict Bradshaw",
		"phone": "+5217307634784",
		"campus": "CSF",
		"career": "LEF",
		"student_number": "a00119503",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Arthur Kelly",
		"phone": "+5218779688211",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a08621861",
		"career exam": "0",
		"CENEVAL": "1",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "0",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Carter Skinner",
		"phone": "+5219786270625",
		"campus": "CCM",
		"career": "LIN",
		"student_number": "a05571813",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "1"
	},
	{
		"name": "Simon Dejesus",
		"phone": "+5210242154690",
		"campus": "CCM",
		"career": "LAF",
		"student_number": "a00823159",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "1",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Basil Weeks",
		"phone": "+5211972698941",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a01141759",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Amanda Mendez",
		"phone": "+5210160032116",
		"campus": "CSF",
		"career": "LIN",
		"student_number": "a01047546",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Shelby Kent",
		"phone": "+5217684122780",
		"campus": "CSF",
		"career": "IMT",
		"student_number": "a01279026",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Abbot Wade",
		"phone": "+5216545456530",
		"campus": "CCM",
		"career": "LEF",
		"student_number": "a00598562",
		"career exam": "1",
		"CENEVAL": "1",
		"e sign": "1",
		"education credit": "1",
		"english exam": "0",
		"financial services": "1",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "1"
	},
	{
		"name": "Jaime Blackwell",
		"phone": "+5210774527836",
		"campus": "CEM",
		"career": "LAF",
		"student_number": "a03659233",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "0",
		"financial services": "0",
		"graduation request": "1",
		"library": "0",
		"photography": "0",
		"program": "1",
		"social service": "0"
	},
	{
		"name": "Jaden Chase",
		"phone": "+5210030889888",
		"campus": "CCM",
		"career": "IDS",
		"student_number": "a05154118",
		"career exam": "1",
		"CENEVAL": "0",
		"e sign": "0",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "1",
		"library": "1",
		"photography": "1",
		"program": "0",
		"social service": "0"
	},
	{
		"name": "Kylie Mcpherson",
		"phone": "+5217421023217",
		"campus": "CEM",
		"career": "IDS",
		"student_number": "a00057736",
		"career exam": "0",
		"CENEVAL": "0",
		"e sign": "1",
		"education credit": "0",
		"english exam": "1",
		"financial services": "0",
		"graduation request": "0",
		"library": "1",
		"photography": "1",
		"program": "1",
		"social service": "0"
	}
]

dbController = mongoController()
dbController.connect_mongo()

for student in students:
    student["mail"] = student["student_number"]+"@itesm.mx"
    dbController.create("students",student)


dbController.to_int( "students" )