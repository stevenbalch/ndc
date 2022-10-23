#!/usr/bin/tclsh

# name:		cgilib.tcl
# author:	John Norton
# created:	04/15/98
# modified:	04/16/98

#--------------------------------------------------#
# sub that parses and cleans up CGI name/val pairs #
#--------------------------------------------------#

proc Clean_Cgi {buf} {

	#-----------------------------------------------#
	# unescape characters escaped by the web server #
	#-----------------------------------------------#

	regsub -all {\\(.)} $buf {\1} buf 
	
	#-----------------------------------#
	# escape dangerous characters [ $ " #
	#-----------------------------------#

	regsub -all {([[$"])} $buf {\\\1} buf

	#---------------------------------------------------#
	# translate "+" (plus sign) into " " (white space)  #
	#---------------------------------------------------#

	regsub -all {\+} $buf { } buf

	#-------------------------------------------#
	# parse the data in buf into correct format #
	#-------------------------------------------#

	regsub -all -nocase {%([a-fA-F0-9][a-fA-F0-9])} $buf {[format %c 0x\1]} buf

	#--------------------------------------#
	# now return buf in its "treated" form #
	#--------------------------------------#

	eval return \"$buf\"
}

#-----------------------------------------------------------------------------#
# sub that parses MESSAGE and places the name/value pairs into the cgi array. #
#-----------------------------------------------------------------------------#

proc parse_cgi_message { MESSAGE } {
	global cgi
	
	set cgi() ""

	#-------------------------------------------------------------#
	# split MESSAGE on the "&" character and process each element #
	#-------------------------------------------------------------#
	
	foreach pair [split $MESSAGE &] {

		#---------------------------------------------#
		# split the current pair on the "=" character #
		#---------------------------------------------#

		set plst [split $pair =]

		#-------------------------------------------------------#
		# assign variables "name" and "val" from the split pair #
		#-------------------------------------------------------#

		set name [Clean_Cgi [lindex $plst 0]]
		set val  [Clean_Cgi [lindex $plst 1]]

		#---------------------------------------------------------#
		# now append "val" to the cgi array as the "name" element #
		#---------------------------------------------------------#

		lappend cgi($name) $val
	}
}

#-------------------------------------------------------------------#
# sub that displays the contents of ARRAY as an HTML table - useful #
# for troubleshooting CGI scripts                                   #
#-------------------------------------------------------------------#

proc display_array { ARRAY } {
	global $ARRAY 

	set list [array get $ARRAY]

	set x 1

	if {[llength $list] > 0} {
		puts "<h4><font color=\"#0000ff\">Contents of \"$ARRAY\" array</font></h4>"
		puts "<table cellspacing=3 border=1>"
		puts "<tr><th align=left>Variable</th><th align=left>Value</th></tr>"

		foreach item [set list] {
			if {$x == 1} {
				puts -nonewline "<tr><td><b>$item</b></td>"
				set x 2
			} else {
				puts "<td><b><font color=\"#0000ff\">$item</font></b></td></tr>"
				set x 1
			}
		}

		puts "</table>"
	}
}

proc check_method {} {
	global env message

	if {[string compare $env(REQUEST_METHOD) "POST"] == 0} {
		set message [read stdin $env(CONTENT_LENGTH)];
	} else {
		set message $env(QUERY_STRING)
	}
}

proc print_header {} {
	puts "Content-type: text/html\n"
}
