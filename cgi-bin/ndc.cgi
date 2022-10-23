#!/usr/bin/tclsh

# Name     :    ndc.cgi
# Author   :    Steven W. Balch
# Created  :    08/26/04
# Version  :    1.00 Alpha RC2

# -----------------------------------------------
# CGI Variables
source "cgilib.tcl"
check_method
parse_cgi_message $message
print_header
# -----------------------------------------------
# Top Header
# -----------------------------------------------
puts {<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">}
puts {<HTML><HEAD><TITLE>NDC -- Network Device Configurator</TITLE>}
puts {<META http-equiv=Content-Type content="text/html; charset=windows-1252">}
puts {<link rel="shortcut icon" href="../icons/favicon.ico" mce_href=”../icons/favicon.ico”/>}
puts {</HEAD>}
puts {<BODY text=#000000 vLink=#0000FF aLink=#0000FF link=#0000FF bgColor=#ffffff>}
puts {<TABLE cellSpacing=0 cellPadding=0 bgColor=#ffffff border=0>}
puts {<TBODY>}
puts {<TR>}
puts {<TD vAlign=center borderColor=#ffffff align=left width="107" rowSpan=3>}
puts {<img border="0" src="../icons/packet.png"</TD>}
puts {<TD vAlign=top borderColor=#ffffff align=right width="100%">}
puts {<p align="center">&nbsp;</TD></TR>}
puts {<TR>}
puts {<TD vAlign=top borderColor=#ffffff align=middle width="100%">}
puts {<P align=center><b><font face="Arial" size="5">N | D | C</font></b></P></TD></TR>}
puts {<TR>}
puts {<TD vAlign=top borderColor=#ffffff align=right width="100%"><FONT class=smdefault_white></FONT>}
puts {<P align=center><font size="2"><i>Network Device Command and Control</i></font></P></TD></TR></TBODY></TABLE>}
puts {<DIV align=left>}
puts {<TABLE height=10 cellSpacing=0 cellPadding=0 width="100%" bgColor=#000000 border=0><TBODY>}
puts {<TR>}
puts {<TD borderColor=#ffffff bgColor=#ffffff height="0">}
puts {<hr color="#000000">}
puts {</TD></TR></TBODY></TABLE></DIV>}
puts {<TABLE cellSpacing=0 cellPadding=5 width="100%" border=0 height="100%">}
puts {<TBODY>}
puts {<TR>}
puts {<TD vAlign=top width="20%" bgColor=#ffffff height="100%">}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6"><STRONG><FONT SIZE=2><img src="../icons/rd_tri.gif" border=0 width="20" height="10"><a href="ndc.cgi">Index</a></FONT></STRONG></P>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">&nbsp;</P>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6"><STRONG><FONT SIZE=2><img border="0" src="../icons/bl_tri.gif" width="20" height="10">Policy Management</FONT></STRONG></P>}
puts {<ul>}
puts {<li>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">}
puts {<strong><font size="2"><a href="ndc.cgi?newdevice">New Device</a></font></strong></P>}
puts {</li>}
puts {<li>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">}
puts {<strong><font size="2"><a href="ndc.cgi?opendevice">Open Device</a></font></strong></P>}
puts {</li>}
puts {<li>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">}
puts {<strong><font size="2"><a href="ndc.cgi?deletedevice">Delete Device</a></font></strong></P>}
puts {</li>}
puts {<li>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">}
puts {<strong><font size="2"><a href="ndc.cgi?openarchive">Open Archive</a></font></strong></P>}
puts {</li>}
puts {<li>}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">}
puts {<strong><font size="2"><a href="ndc.cgi?deletearchive">Delete Archive</a></font></strong></P>}
puts {}
puts {<P style="word-spacing: 0; line-height: 100%; margin-top: 6; margin-bottom: 6">&nbsp;</P>}
puts {</td>}
puts {<TD vAlign=top align=left width=1 height="100%">}
puts {<img border="0" src="../icons/bar9ver.gif" width="5" height="90%"></TD>}
puts {<TD vAlign=top width="100%" height="100%">}
puts {<b>N | D | C - <u>N</u>etwork <u>D</u>evice <u>C</u>onfigurator -- 1.00 Alpha RC2</b>}

# -----------------------------------------------
# End of Header
# -----------------------------------------------
# -----------------------------------------------
# Start of Utility
# -----------------------------------------------

# -----------------------------------------------
# Start of Index Procedure
# -----------------------------------------------
proc indexp {} {
global env cgi

puts {<p><font size="2">Centrally manage changes to routers, switches, firewalls, load balancers, and other network devices via a simple web based command line automation tool. -- N | D | C</font></p>}
puts {<hr color="#000000">}


# -----------------------------------------------           
# End of Index Procedure
               }
# -----------------------------------------------
              
# -----------------------------------------------
# Start of New Device Procedure
# ----------------------------------------------- 
proc newdevicep {} {
global env cgi

puts "<form action=\"ndc.cgi?create=newdevice\" method=\"POST\">"

if {[regexp {create=newdevice} $env(QUERY_STRING)] == 1} {
	
set devpoldir ../policy/device-policy

if [catch {exec touch $devpoldir/$cgi(new).policy} err] {
puts "Unable to Create Policy"
                                                        }
                                                     
if [catch {exec chmod 777 $devpoldir/$cgi(new).policy} err] {
puts "Unable to Change Policy Permissions"
                                                            }
                                                                                                                                      
puts "<p><strong>Policy Created:</strong><i>&nbsp;$cgi(new)</i></p>"

puts {<hr color="#000000">}				

} else {

puts "<p><input type=\"text\" name=\"new\" id=\"new\" size=\"30\""
puts "<p><strong> Device Name </strong><i>&lt;DNS Name&gt;</i></p>"

puts {<input type="submit" name="create" id="create" value="Create Device Policy"></p>}
puts {</form>}

puts {<hr color="#000000">}

       }
# -----------------------------------------------           
# End of New Device Procedure
                   }
# -----------------------------------------------	

# -----------------------------------------------
# Start of Open Device Procedure
# ----------------------------------------------- 
proc opendevicep {} {
global env cgi

puts "<form action=\"ndc.cgi\" method=\"GET\">"

set devpoldir ../policy/device-policy

if [catch {set rlist1 [glob $devpoldir/*]} err] {
puts $err
                                                }
                                               
set rlist [lsort -ascii $rlist1]                                               

puts "<select name=\"dpolicy\" id=\"dpolicy\" size=\"1\">"

foreach entry $rlist {

set var1 [split $entry {/}]
set var2 [lindex $var1 3]

puts "<option value=\"$var2\" selected>$var2</option>"

                     }                                                               
puts {</select>}
puts "<input type=\"submit\" value=\"Open Device Policy\">"
puts {&nbsp;</form>}

puts {<hr color="#000000">}

# -----------------------------------------------           
# End of Open Device Procedure
                    }
# -----------------------------------------------
	
# -----------------------------------------------
# Start of File Open Procedure
# ----------------------------------------------- 
proc fopen {} {
global env cgi

set devpoldir ../policy/device-policy
set devpoldirsave ../policy/saved-policy

set spline [split $env(QUERY_STRING) {=}]
set qsrw [lindex $spline 1]

puts "<form action=\"ndc.cgi?$env(QUERY_STRING)\" method=\"POST\">"

#display_array cgi
#display_array env

set time [clock format [clock seconds] -format %d%b%Y-%H%M]


if {[info exists cgi(file)] ==1} {

set datarw1 [string trim $cgi(file) \{]
set datarw2 [string trim $datarw1 \}]
set datarw3 [string trimright $datarw2 \^M]
set data [string trim $datarw3 ]


if [catch {exec cp $devpoldir/$qsrw $devpoldirsave/$qsrw.$time} err] {
#puts "$err"
puts "Unable to Create Backup Copy of <i>$qsrw</i>"
                                                                     }
                                                                     
if [catch {exec echo $data > $devpoldir/$qsrw} err] {
#puts "$err"
puts "Unable to Save Policy <i>$qsrw</i>"
                                                    } 

                                 }


set policyfile [open $devpoldir/$qsrw r]

puts "<p><font size=\"2\"><b>Command Line Window for:</b> <i>$qsrw</i></font></p>"

puts "<p><textarea name=\"file\" id=\"file\" rows=\"25\" size=\"500000\" cols=\"120\" wrap=off>"

while {[gets $policyfile entry] >= 0} {


puts "$entry"
                                      }
puts {</textarea></p>}
puts "<input type=\"submit\" name=\"Save\" id=\"Save\" value=\"Save\"></p>"
puts {<p><a href="ndc.cgi?opendevice"><img border="0" src="../icons/backg.gif" width="42" height="41"></a><strong> Go Back</strong>}
puts {&nbsp;}
puts {&nbsp;}
puts "<a href=\"ndc.cgi?fconfp?$env(QUERY_STRING)\"><img border=\"0\" src=\"../icons/pushg.gif\" width=\"42\" height=\"41\"></a><strong> Push Current Policy to Device</strong></p>"
puts {</form>}

puts {<hr color="#000000">}

# -----------------------------------------------
# End of File Open Procedure     
              }
# -----------------------------------------------

# -----------------------------------------------
# Start of File Push Procedure
# ----------------------------------------------- 
proc fconfp {} {
global env cgi

set devpoldir ../policy/device-policy
set bindir ../bin

set spline [split $env(QUERY_STRING) {?}]
set qsrw1 [lindex $spline 1]
set spline2 [split $qsrw1 {=}]
set qsrw2 [lindex $spline2 1]
#set spline3 [string trimright $qsrw2 {.policy}]
regsub {.policy} $qsrw2 {} spline3
set qsrw [lindex $spline3 0]

if {[info exists cgi(Submit)] ==1} {
	
#puts "<p>$cgi(EPASSWORD)</p>"
#puts "<p>$cgi(USERNAME)</p>"
#puts "<p>$cgi(EPASSTATUS)</p>"
#puts "<p>$cgi(UNAMESTATUS)</p>"
#puts "<p>$cgi(ACCESS)</p>"
#puts "<p>$cgi(PASSWORD)</p>"

if {[regexp {no} $cgi(UNAMESTATUS)] == 1} {
set cgi(USERNAME) NONE
                                          }
                                          
if {[regexp {no} $cgi(EPASSTATUS)] == 1} {
set cgi(EPASSWORD) NONE
                                         }

if [catch {eval exec $bindir/ndc.exp $devpoldir/$qsrw2 $qsrw $cgi(ACCESS) $cgi(UNAMESTATUS) $cgi(USERNAME) $cgi(PASSWORD) $cgi(EPASSTATUS) $cgi(EPASSWORD) > /dev/null 2> /dev/null &} err] {
puts "Unable to Deploy Policy: $qsrw2 to $qsrw"
} else {
	
#display_array cgi
#display_array env

#puts "<p>This will be the command</p>"
#puts "<p>exec $bindir/ndc.exp $devpoldir/$qsrw2 $qsrw $cgi(ACCESS) $cgi(UNAMESTATUS) $cgi(USERNAME) $cgi(PASSWORD) $cgi(EPASSTATUS) $cgi(EPASSWORD) > /dev/null 2> /dev/null &</p>"

puts "<p><strong>Policy is now being Deployed to:</strong><i>&nbsp;$qsrw</i></p>"
puts {<p></p>}
puts {<p></p>}
puts "<p><i>Note:&nbsp;</i>This will take a few minutes to complete.</p>"
       }
puts "<p><a href=\"ndc.cgi?$env(QUERY_STRING)\"><img border=\"0\" src=\"../icons/backg.gif\" width=\"42\" height=\"41\"></a><strong> Go Back</strong></p>"

puts {<hr color="#000000">}


} else {

puts "<form action=\"ndc.cgi?$env(QUERY_STRING)\" method=\"POST\">"

puts "<p>How would you like to access the device?"
puts "<input type=\"radio\" value=\"telnet\" name=\"ACCESS\" id=\"ACCESS\" checked />Telnet"
puts "<input type=\"radio\" value=\"ssh\" name=\"ACCESS\" id=\"ACCESS\"  />SSH"
puts "</p>"
puts "<p>Does the device require a username?"
puts "<input type=\"radio\" value=\"yes\" name=\"UNAMESTATUS\" id=\"UNAMESTATUS\" />Yes"
puts "<input type=\"radio\" value=\"no\" name=\"UNAMESTATUS\" id=\"UNAMESTATUS\"  checked />No"
puts "<input type=\"text\" name=\"USERNAME\" id=\"USERNAME\" size=\"30\""
puts "</p>"
puts "<p>What is the device password?"
puts "<input type=\"password\" name=\"PASSWORD\" id=\"PASSWORD\" size=\"30\""
puts "</p>"
puts "<p>Does the device require an enable password?"
puts "<input type=\"radio\" value=\"yes\" name=\"EPASSTATUS\" id=\"EPASSTATUS\" checked />Yes"
puts "<input type=\"radio\" value=\"no\" name=\"EPASSTATUS\" id=\"EPASSTATUS\"  />No"
puts "<input type=\"password\" name=\"EPASSWORD\" id=\"EPASSWORD\" size=\"30\""
puts "</p>"

puts "<p><input type=\"submit\" name=\"Submit\" id=\"Submit\" value=\"Submit\">"
puts "<strong>&nbsp;Push Current Policy to Device:</strong> <i>$qsrw</i></p>"

puts {</form>}

puts "<p><a href=\"ndc.cgi?$qsrw1\"><img border=\"0\" src=\"../icons/backg.gif\" width=\"42\" height=\"41\"></a><strong> Go Back</strong></p>"

puts {<hr color="#000000">}

#display_array cgi
#display_array env
       }
# -----------------------------------------------
               }
# End of File Push Procedure
# -----------------------------------------------
	
# -----------------------------------------------
# Start of Delete Device Procedure
# ----------------------------------------------- 
proc deletedevicep {} {
global env cgi

puts "<form action=\"ndc.cgi\" method=\"GET\">"

set devpoldir ../policy/device-policy

if [catch {set rlist1 [glob $devpoldir/*]} err] {
puts $err
                                                }
                                               
set rlist [lsort -ascii $rlist1]                                               

puts "<select name=\"rpolicy\" id=\"rpolicy\" size=\"1\">"

foreach entry $rlist {

set var1 [split $entry {/}]
set var2 [lindex $var1 3]

puts "<option value=\"$var2\" selected>$var2</option>"

                     }                                                               
puts {</select>}
puts "<input type=\"submit\" value=\"Delete Device Policy\">"
puts {&nbsp;</form>}

puts {<hr color="#000000">}

# -----------------------------------------------           
# End of Delete Device Procedure
                    }
# -----------------------------------------------

# -----------------------------------------------
# Start of File Delete Procedure
# ----------------------------------------------- 
proc fdelete {} {
global env cgi

set devpoldir ../policy/device-policy

set spline [split $env(QUERY_STRING) {=}]
set qsrw [lindex $spline 1]


puts "<form action=\"ndc.cgi?$env(QUERY_STRING)\" method=\"POST\">"

#display_array cgi
#display_array env

                                                                  
if [catch {exec rm $devpoldir/$qsrw} err] {
#puts "$err"
puts "Unable to Delete Policy <i>$qsrw</i>"
                                           } 


puts "<p><font size=\"2\"><b>Device Policy: </b><i>$qsrw</i> <b>has been deleted.</b></font></p>"


puts {<p><a href="ndc.cgi?deletedevice"><img border="0" src="../icons/backg.gif" width="42" height="41"></a><strong> Go Back</strong>}
puts {&nbsp;}
puts {&nbsp;}

puts {</form>}

puts {<hr color="#000000">}

# -----------------------------------------------
# End of File Delete Procedure     
              }
# -----------------------------------------------

# -----------------------------------------------
# Start of Open Archive Procedure
# ----------------------------------------------- 
proc openarchivep {} {
global env cgi

puts "<form action=\"ndc.cgi\" method=\"GET\">"

set devpoldir ../policy/saved-policy

if [catch {set rlist1 [glob $devpoldir/*]} err] {
puts $err
                                                }
                                               
set rlist [lsort -ascii $rlist1]                                               

puts "<select name=\"apolicy\" id=\"apolicy\" size=\"1\">"

foreach entry $rlist {

set var1 [split $entry {/}]
set var2 [lindex $var1 3]

puts "<option value=\"$var2\" selected>$var2</option>"

                     }                                                               
puts {</select>}
puts "<input type=\"submit\" value=\"Open Archive Policy\">"
puts {&nbsp;</form>}

puts {<hr color="#000000">}

# -----------------------------------------------           
# End of Open Archive Procedure
                    }
# -----------------------------------------------

# -----------------------------------------------
# Start of File Archive Open Procedure
# ----------------------------------------------- 
proc aopen {} {
global env cgi

set devpoldir ../policy/saved-policy

set spline [split $env(QUERY_STRING) {=}]
set qsrw [lindex $spline 1]

set spline2 [split $qsrw {.}]
set qsrw2 [lindex $spline2 0]

puts $qsrw2

puts "<form action=\"ndc.cgi?$env(QUERY_STRING)\" method=\"POST\">"

#display_array cgi
#display_array env

if {[info exists cgi(file)] ==1} {

set datarw1 [string trim $cgi(file) \{]
set datarw2 [string trim $datarw1 \}]
set datarw3 [string trimright $datarw2 \^M]
set data [string trim $datarw3 ]

                                                                     
if [catch {exec echo $data > $devpoldir/$qsrw} err] {
#puts "$err"
puts "Unable to Save Policy <i>$qsrw</i>"
                                                    } 

                                 }

set policyfile [open $devpoldir/$qsrw r]

puts "<p><font size=\"2\"><b>Command Line Window for:</b> <i>$qsrw</i></font></p>"

puts "<p><textarea name=\"file\" id=\"file\" rows=\"25\" size=\"500000\" cols=\"120\" wrap=off>"

while {[gets $policyfile entry] >= 0} {


puts "$entry"
                                      }
puts {</textarea></p>}
puts "<input type=\"submit\" name=\"Save\" id=\"Save\" value=\"Save\"></p>"
puts {<p><a href="ndc.cgi?openarchive"><img border="0" src="../icons/backg.gif" width="42" height="41"></a><strong> Go Back</strong>}
puts {&nbsp;}
puts {&nbsp;}
puts {</form>}

puts {<hr color="#000000">}

# -----------------------------------------------
# End of File Archive Open Procedure     
              }
# -----------------------------------------------

# -----------------------------------------------
# Start of Delete Archive Device Procedure
# ----------------------------------------------- 
proc deletearchivep {} {
global env cgi

puts "<form action=\"ndc.cgi\" method=\"GET\">"

set devpoldir ../policy/saved-policy

if [catch {set rlist1 [glob $devpoldir/*]} err] {
puts $err
                                                }
                                               
set rlist [lsort -ascii $rlist1]                                               

puts "<select name=\"arpolicy\" id=\"arpolicy\" size=\"1\">"

foreach entry $rlist {

set var1 [split $entry {/}]
set var2 [lindex $var1 3]

puts "<option value=\"$var2\" selected>$var2</option>"

                     }                                                               
puts {</select>}
puts "<input type=\"submit\" value=\"Delete Archive Device Policy\">"
puts {&nbsp;</form>}

puts {<hr color="#000000">}

# -----------------------------------------------           
# End of Delete Archive Device Procedure
                    }
# -----------------------------------------------

# -----------------------------------------------
# Start of File Archive Delete Procedure
# ----------------------------------------------- 
proc adelete {} {
global env cgi

set devpoldir ../policy/saved-policy

set spline [split $env(QUERY_STRING) {=}]
set qsrw [lindex $spline 1]


puts "<form action=\"ndc.cgi?$env(QUERY_STRING)\" method=\"POST\">"

#display_array cgi
#display_array env

                                                                  
if [catch {exec rm $devpoldir/$qsrw} err] {
#puts "$err"
puts "Unable to Delete Policy <i>$qsrw</i>"
                                           } 


puts "<p><font size=\"2\"><b>Archive Device Policy: </b><i>$qsrw</i> <b>has been deleted.</b></font></p>"


puts {<p><a href="ndc.cgi?deletearchive"><img border="0" src="../icons/backg.gif" width="42" height="41"></a><strong> Go Back</strong>}
puts {&nbsp;}
puts {&nbsp;}

puts {</form>}

puts {<hr color="#000000">}

# -----------------------------------------------
# End of File Archive Delete Procedure     
              }
# -----------------------------------------------


# -----------------------------------------------           
# Start of Core Processes
# -----------------------------------------------

if {[regexp {newdevice} $env(QUERY_STRING)] == 1} {
newdevicep
} else {
if {[regexp {opendevice} $env(QUERY_STRING)] == 1} {	
opendevicep
} else {
if {[regexp {^dpolicy=} $env(QUERY_STRING)] == 1} {
fopen
} else {	
if {[regexp {^fconfp} $env(QUERY_STRING)] == 1} {
fconfp
} else {
if {[regexp {deletedevice} $env(QUERY_STRING)] == 1} {	
deletedevicep
} else {
if {[regexp {^rpolicy=} $env(QUERY_STRING)] == 1} {	
fdelete
} else {
if {[regexp {openarchive} $env(QUERY_STRING)] == 1} {
openarchivep
} else {	
if {[regexp {^apolicy=} $env(QUERY_STRING)] == 1} {	
aopen
} else {
if {[regexp {deletearchive} $env(QUERY_STRING)] == 1} {	
deletearchivep
} else {
if {[regexp {^arpolicy=} $env(QUERY_STRING)] == 1} {
adelete					
} else {
indexp
       }
       }
       }
       }
       }
       }
       }
       }
       }
       }
# -----------------------------------------------          
# End of Core Processes
# -----------------------------------------------

# -----------------------------------------------          
# End of HTML
# -----------------------------------------------
puts {</TD></TR></TBODY></TABLE></BODY></HTML>}
# -----------------------------------------------

# -----------------------------------------------          
# Done
# -----------------------------------------------
