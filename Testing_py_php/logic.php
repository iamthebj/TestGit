<?php
                //$planquery="SELECT * FROM plan";
                $dquery= "SELECT * FROM details";
                $device = $_POST['device'];
                $provider1 = $_POST['provider1'];
                //$provider2 = $_POST['provider2'];
                //$provider3 = $_POST['provider3'];
                //$provider4 = $_POST['provider4'];
                $plantype = $_POST['plantype'];
                $dusage = $_POST['dusage'];
                $cusage = $_POST['cusage'];
                $musage = $_POST['musage'];
                $planquery="SELECT * FROM plan WHERE 
                            Phone='$device' AND SIMTYPE='$plantype' AND 'DATA'>='$dusage' AND 'CALL'>='$cusage' AND 'MSG'>='$musage' "; 
                $planresult=mysql_query($planquery) or die ("Query to get data from firsttable failed: ".mysql_error());
                $dresult=mysql_query($dquery) or die ("Query to get data from firsttable failed: ".mysql_error());
                //$sresult=mysql_query($squery) or die ("Query to get data from firsttable failed: ".mysql_error());
                while ((($prow = mysql_fetch_assoc($planresult))) && ($drow = mysql_fetch_assoc($dresult)) ) {

                ?>