def list_fill():	
	global first_middle, middle_initial, dob, last_name
	first_middle = ["ZZ", "ZY", "ZX", "ZW", "ZV", "ZU", "ZT", "ZS", "ZR", "ZQ", "ZP", "ZO", "ZN", "ZM", "ZL", "ZK", "ZJ", "ZI", "ZH", "ZG", "ZF", "ZE", "ZD", "ZC", "ZB", "ZA", "Z", "YZ", "YY", "YX", "YW", "YV", "YU", "YT", "YS", "YR", "YQ", "YP", "YO", "YN", "YM", "YL", "YK", "YJ", "YI", "YH", "YG", "YF", "YE", "YD", "YC", "YB", "YA", "Y", "XZ", "XY", "XX", "XW", "XV", "XU", "XT", "XS", "XR", "XQ", "XP", "XO", "XN", "XM", "XL", "XK", "XJ", "XI", "XH", "XG", "XF", "XE", "XD", "XC", "XB", "XA", "X", "WZ", "WY", "WX", "WW", "WV", "WU", "WT", "WS", "WR", "WQ", "WP", "WO", "WN", "WM", "WL", "WK", "WJ", "WIZ", "WIY", "WIX", "WIW", "WIV", "WIU", "WIT", "WIS", "WIR", "WIQ", "WIP", "WIO", "WIN", "WIM", "WILLIAM", "WIL", "WIK", "WIJ", "WII", "WIH", "WIG", "WIF", "WIE", "WID", "WIC", "WIB", "WIA", "WI", "WH", "WG", "WF", "WE", "WD", "WC", "WB", "WA", "W", "VZ", "VY", "VX", "VW", "VV", "VU", "VT", "VS", "VR", "VQ", "VP", "VO", "VN", "VM", "VL", "VK", "VJ", "VI", "VH", "VG", "VF", "VE", "VD", "VC", "VB", "VA", "V", "UZ", "UY", "UX", "UW", "UV", "UU", "UT", "US", "UR", "UQ", "UP", "UO", "UN", "UM", "UL", "UK", "UJ", "UI", "UH", "UG", "UF", "UE", "UD", "UC", "UB", "UA", "U", "TZ", "TY", "TX", "TW", "TV", "TU", "TT", "TS", "TR", "TQ", "TP", "TO", "TN", "TM", "TL", "TK", "TJ", "TI", "TH", "TG", "TF", "TE", "TD", "TC", "TB", "TA", "T", "SZ", "SY", "SX", "SW", "SV", "SU", "ST", "SS", "SR", "SQ", "SP", "SO", "SN", "SM", "SL", "SK", "SJ", "SI", "SH", "SG", "SF", "SE", "SD", "SC", "SB", "SA", "S", "RZ", "RY", "RX", "RW", "RV", "RU", "RT", "RS", "RR", "RQ", "RP", "ROBERT", "RO", "RN", "RM", "RL", "RK", "RJ", "RI", "RH", "RG", "RF", "RE", "RD", "RC", "RB", "RA", "R", "QZ", "QY", "QX", "QW", "QV", "QU", "QT", "QS", "QR", "QQ", "QP", "QO", "QN", "QM", "QL", "QK", "QJ", "QI", "QH", "QG", "QF", "QE", "QD", "QC", "QB", "QA", "Q", "PZ", "PY", "PX", "PW", "PV", "PU", "PT", "PS", "PR", "PQ", "PP", "PO", "PN", "PM", "PL", "PK", "PJ", "PI", "PH", "PG", "PF", "PE", "PD", "PC", "PB", "PA", "P", "OZ", "OY", "OX", "OW", "OV", "OU", "OT", "OS", "OR", "OQ", "OP", "OO", "ON", "OM", "OL", "OK", "OJ", "OI", "OH", "OG", "OF", "OE", "OD", "OC", "OB", "OA", "O", "NZ", "NY", "NX", "NW", "NV", "NU", "NT", "NS", "NR", "NQ", "NP", "NO", "NN", "NM", "NL", "NK", "NJ", "NI", "NH", "NG", "NF", "NE", "ND", "NC", "NB", "NA", "N", "MZ", "MY", "MX", "MW", "MV", "MU", "MT", "MS", "MR", "MQ", "MP", "MO", "MN", "MM", "ML", "MK", "MJ", "MI", "MH", "MG", "MF", "ME", "MD", "MC", "MB", "MAZ", "MAY", "MAX", "MAW", "MAV", "MAU", "MAT", "MAS", "MARY", "MARGARET", "MAR", "MAQ", "MAP", "MAO", "MAN", "MAM", "MAL", "MAK", "MAJ", "MAI", "MAH", "MAG", "MAF", "MAE", "MAD", "MAC", "MAB", "MAA", "MA", "M", "LZ", "LY", "LX", "LW", "LV", "LU", "LT", "LS", "LR", "LQ", "LP", "LOZ", "LOY", "LOX", "LOW", "LOV", "LOU", "LOT", "LOS", "LOR", "LOQ", "LOP", "LOO", "LON", "LOM", "LOL", "LOK", "LOJ", "LOI", "LOH", "LOG", "LOF", "LOE", "LOD", "LOC", "LOB", "LOA", "LO", "LN", "LM", "LL", "LK", "LJ", "LI", "LH", "LG", "LF", "LEZ", "LEY", "LEX", "LEW", "LEV", "LEU", "LET", "LES", "LER", "LEQ", "LEP", "LEO", "LEN", "LEM", "LEL", "LEK", "LEJ", "LEI", "LEH", "LEG", "LEF", "LEE", "LED", "LEC", "LEB", "LEA", "LE", "LD", "LC", "LB", "LA", "L", "KZ", "KY", "KX", "KW", "KV", "KU", "KT", "KS", "KR", "KQ", "KP", "KO", "KN", "KM", "KL", "KK", "KJ", "KI", "KH", "KG", "KF", "KE", "KD", "KC", "KB", "KA", "K", "JZ", "JY", "JX", "JW", "JV", "JU", "JT", "JS", "JR", "JQ", "JP", "JOZ", "JOY", "JOX", "JOW", "JOV", "JOU", "JOT", "JOSEPH", "JOS", "JOR", "JOQ", "JOP", "JOO", "JON", "JOM", "JOL", "JOK", "JOJ", "JOI", "JOHN", "JOH", "JOG", "JOF", "JOE", "JOD", "JOC", "JOB", "JOA", "JO", "JN", "JM", "JL", "JK", "JJ", "JI", "JH", "JG", "JF", "JEZ", "JEY", "JEX", "JEW", "JEV", "JEU", "JET", "JES", "JER", "JEQ", "JEP", "JEO", "JEN", "JEM", "JEL", "JEK", "JEJ", "JEI", "JEH", "JEG", "JEF", "JEE", "JED", "JEC", "JEB", "JEA", "JE", "JD", "JC", "JB", "JAZ", "JAY", "JAX", "JAW", "JAV", "JAU", "JAT", "JAS", "JAR", "JAQ", "JAP", "JAO", "JAN", "JAMES", "JAM", "JAL", "JAK", "JAJ", "JAI", "JAH", "JAG", "JAF", "JAE", "JAD", "JAC", "JAB", "JAA", "JA", "J", "IZ", "IY", "IX", "IW", "IV", "IU", "IT", "IS", "IR", "IQ", "IP", "IO", "IN", "IM", "IL", "IK", "IJ", "II", "IH", "IG", "IF", "IE", "ID", "IC", "IB", "IA", "I", "HZ", "HY", "HX", "HW", "HV", "HU", "HT", "HS", "HR", "HQ", "HP", "HO", "HN", "HM", "HL", "HK", "HJ", "HI", "HH", "HG", "HF", "HENRY", "HE", "HD", "HC", "HB", "HA", "H", "GZ", "GY", "GX", "GW", "GV", "GU", "GT", "GS", "GR", "GQ", "GP", "GO", "GN", "GM", "GL", "GK", "GJ", "GI", "GH", "GG", "GF", "GE", "GD", "GC", "GB", "GA", "G", "FZ", "FY", "FX", "FW", "FV", "FU", "FT", "FS", "FR", "FQ", "FP", "FO", "FN", "FM", "FL", "FK", "FJ", "FI", "FH", "FG", "FF", "FE", "FD", "FC", "FB", "FA", "F", "EZ", "EY", "EX", "EW", "EV", "EU", "ET", "ES", "ER", "EQ", "EP", "EO", "EN", "EM", "ELZ", "ELY", "ELX", "ELW", "ELV", "ELU", "ELT", "ELS", "ELR", "ELQ", "ELP", "ELO", "ELN", "ELM", "ELLEN", "ELL", "ELK", "ELJ", "ELIZABETH", "ELI", "ELH", "ELG", "ELF", "ELE", "ELD", "ELC", "ELB", "ELA", "EL", "EK", "EJ", "EI", "EH", "EG", "EF", "EE", "EDZ", "EDY", "EDX", "EDWARD", "EDW", "EDV", "EDU", "EDT", "EDS", "EDR", "EDQ", "EDP", "EDO", "EDN", "EDM", "EDL", "EDK", "EDJ", "EDI", "EDH", "EDG", "EDF", "EDE", "EDD", "EDC", "EDB", "EDA", "ED", "EC", "EB", "EA", "E", "DZ", "DY", "DX", "DW", "DV", "DU", "DT", "DS", "DR", "DQ", "DP", "DO", "DN", "DM", "DL", "DK", "DJ", "DI", "DH", "DG", "DF", "DE", "DD", "DC", "DB", "DA", "D", "CZ", "CY", "CX", "CW", "CV", "CU", "CT", "CS", "CR", "CQ", "CP", "CO", "CN", "CM", "CL", "CK", "CJ", "CI", "CH", "CG", "CF", "CE", "CD", "CC", "CB", "CA", "C", "BZ", "BY", "BX", "BW", "BV", "BU", "BT", "BS", "BR", "BQ", "BP", "BO", "BN", "BM", "BL", "BK", "BJ", "BI", "BH", "BG", "BF", "BE", "BD", "BC", "BB", "BA", "B", "AZ", "AY", "AX", "AW", "AV", "AU", "AT", "AS", "AR", "AQ", "AP", "AO", "AN", "AM", "ALZ", "ALY", "ALX", "ALW", "ALV", "ALU", "ALT", "ALS", "ALR", "ALQ", "ALP", "ALO", "ALN", "ALM", "ALL", "ALK", "ALJ", "ALI", "ALH", "ALG", "ALF", "ALE", "ALD", "ALC", "ALB", "ALA", "AL", "AK", "AJ", "AI", "AH", "AG", "AF", "AE", "AD", "AC", "AB", "AA", "A"]
	middle_initial = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	dob = [["002", "007", "010", "012", "017", "020", "022", "025", "027", "030", "032", "035", "037", "040", "042", "045", "047", "050", "052", "055", "057", "060", "062", "065", "067", "070", "072", "075", "077", "080", "082"], ["086", "088", "091", "093", "096", "098", "101", "103", "106", "108", "111", "113", "116", "118", "121", "123", "126", "128", "131", "133", "136", "138", "141", "143", "146", "148", "151", "153", "156"], ["159", "162", "164", "167", "169", "172", "174", "177", "182", "184", "187", "189", "192", "194", "197", "199", "202", "204", "207", "227", "229", "232", "234", "237", "239", "242", "244", "247", "249", "252", "254"], ["258", "260", "263", "265", "268", "270", "273", "275", "278", "280", "283", "285", "288", "290", "293", "295", "298", "300", "303", "305", "308", "310", "313", "315", "318", "320", "323", "325", "328", "330"], ["334", "336", "339", "341", "344", "346", "349", "351", "354", "356", "359", "361", "364", "366", "369", "371", "374", "376", "379", "381", "384", "386", "389", "391", "394", "396", "399", "401", "404", "406", "409"], ["412", "415", "417", "420", "422", "425", "427", "430", "432", "435", "437", "440", "442", "445", "447", "450", "452", "467", "470", "472", "475", "477", "480", "482", "497", "500", "502", "505", "507", "517"], ["521", "523", "526", "528", "534", "537", "539", "542", "544", "547", "549", "552", "554", "557", "559", "562", "564", "567", "569", "572", "574", "577", "579", "582", "584", "587", "589", "592", "594", "597", "599"], ["603", "605", "608", "610", "613", "615", "618", "620", "623", "625", "628", "630", "633", "635", "638", "640", "643", "645", "648", "650", "653", "655", "658", "660", "663", "665", "668", "670", "673", "675", "678"], ["681", "684", "686", "689", "691", "694", "696", "699", "701", "704", "706", "709", "711", "714", "716", "719", "721", "724", "726", "729", "731", "734", "736", "739", "741", "744", "746", "749", "751", "754"], ["757", "760", "762", "765", "767", "770", "772", "775", "777", "780", "782", "785", "787", "790", "792", "797", "800", "802", "807", "810", "812", "815", "817", "820", "822", "825", "827", "830", "832", "835", "837"], ["841", "843", "846", "848", "851", "853", "856", "858", "861", "863", "866", "868", "871", "873", "876", "878", "881", "883", "886", "888", "891", "893", "896", "898", "901", "903", "906", "908", "911", "913"], ["917", "919", "922", "924", "927", "929", "932", "934", "937", "939", "942", "944", "947", "949", "952", "954", "957", "959", "962", "964", "967", "969", "972", "974", "977", "983", "985", "990", "993", "995", "998"]]
	last_name = [["A", "E", "H", "I", "O", "U", "W", "Y"],["B", "F", "P", "V"], ["C", "G", "J", "K", "Q", "S", "X", "Z"], ["D", "T"], ["L"], ["M", "N"], ["R"]]
#########################################################################################
from os import system, path, get_terminal_size
window_width = get_terminal_size().columns

from datetime import date
today = date.today().strftime("%B %d, %Y")
#########################################################################################
def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}". format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
#########################################################################################
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
#########################################################################################
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
#########################################################################################
def formating_process(phrase1,phrase2):
	return print(center("{0:<30} {1:<20}".format(phrase1,phrase2)))
#########################################################################################
def error_correcting (ans):
	if (ans == "" or not ans[0].isalpha()):
		print(ans, "is an invalid entry ")
		return True
	else: 
		return False
#########################################################################################	
def number_error_correcting(ans):
	if (not ans.isdigit()) or (int(ans) <1) or (int(ans)>12):
		print(ans, "is an invalid entry ")
		return True
	else: 
		return False
#########################################################################################
def day_error_correcting(ans):
	if (not ans.isdigit()) or (int(ans) <1) or (int(ans)>len(dob[int(answers[3])-1])):
		print(ans, "is an invalid entry ")
		return True
	else: 
		return False
#########################################################################################

def input_license():
	global questions, answers
	questions = ["Enter in the first name: ","Enter in the middle name: ","Enter in the last name: ","Enter in the month of birth: ","Enter in the date of birth: "]
	answers = ["","","","",""]
	i = 0
	while i in range(len(questions)):
		answers[i]=input_center("{0:<30}".format(questions[i])).upper()
		if i == 0 or i == 2:
			if (error_correcting(answers[i])):
				i -= 1
		if i == 3:
			if (number_error_correcting(answers[i])):
				i -= 1		
		if i == 4:
			if (day_error_correcting(answers[i])):
				i -= 1
		i +=1
		
def process_license():
	global final
	ln = ["","","","000",""]
	final =["","",""]
	no_middle = ""
	# last name
	for y in range(len(answers[2])):
		if y == 0:
			ln[0] = answers[2][y]
		else:
			for r in range(len(last_name)):
				if answers[2][y] in last_name[r]:
					if r != 0:
						ln[1] += str(r)
	#first name & middle initial
	while len(ln[1]) < 3:
		ln[1] = ln[1]+"0"
	for j in range (len(first_middle)):
		if answers[0].startswith(first_middle[j]):
			ln[2]=str(999-j)
			break
	while len(ln[2]) < 3:
		ln[2] = "0"+ln[2]
	if answers[1] == "" and len(answers[0]) > len(first_middle[j]):
		no_middle = answers[0][len(first_middle[j])]
		for i in range (len(middle_initial)):
			if no_middle.startswith(middle_initial[i]):
				ln[3]= str(i+1)
				break
	else:
		for j in range (len(first_middle)):
			if answers[1].startswith(first_middle[j]):
				ln[3]=str(999-j)
				break
	while len(ln[3]) < 3:
		ln[3] = "0"+ln[3]
	#DoB
	ln[4]=dob[int(answers[3])-1][int(answers[4])-1]

	full_name = (answers[0]+" "+answers[1]+" "+answers[2])
	birthdate = (answers[3]+"/"+answers[4])
	license_number = (ln[0]+"-"+ln[1]+"-"+ln[2]+"-"+ln[3]+"-"+ln[4])
	final = [full_name,birthdate,license_number]

def output_license():
	equals_border = ("="*60)
	print("\n\n")
	print(center(equals_border))
	print()
	formating_process("Enter in the first name: ",answers[0]+"\n")
	formating_process("Enter in the middle name: ",answers[1]+"\n")
	formating_process("Enter in the last name: ",answers[2]+"\n")
	formating_process("Enter in the month of birth: ",answers[3]+"\n")
	formating_process("Enter in the date of birth ",answers[4]+"\n")
	print(center(equals_border))
	print("\n\n")
	formating_process("Name: " ,final[0]+"\n")
	formating_process("Born: " ,final[1]+"\n")
	formating_process("License Number: " ,final[2]+"\n\n\n")
	print(center(equals_border))
	print()
	
def main_bus(repeat = "Y"):
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"\n'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == 'y' or repeat == 'Y':
		header()
		list_fill()
		input_license()
		process_license()
		header()
		output_license()
		repeat = input_center("Would you like to run the program again (Y/N): ")
		main_bus(repeat)
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run again (Y/N): ")
		main_bus(repeat)	
main_bus()

# Edin Mehanovic 11/20/2023
# The error correcting portion of this program was a very difficult task to wrap my head around. Figuring out how to use the lists we copy and pasted from our excel sheets was another difficultly I had in the beginning stages of this program. The process itself was enough of a hastle to get through as well. 
# I have a more in-depth knowledge of how lists work, and how I can more easily use them down the line. 