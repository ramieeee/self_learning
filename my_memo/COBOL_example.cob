000000 IDENTIFICATION DIVISION.
000000 PROGRAM-ID.    COBOL_TEST.
000000 ENVIRONMENT DIVISION.
000000 DATA DIVISION.
000000 WORKING-STORAGE SECTION.

000000*----about --init-space option----
000000* --init-space Sets the initial value of variables
000000* It is as simple as switching nulls to spaces
000000*---------------------------------


000000*----------Initialize-------------
000000 01 TEMP PIC X(3).
000000 01 STR.
000000     05 CHR PIC X(2).
000000     05 NUM PIC 9(2) VALUE 0.
000000*---------------------------------


000000 PROCEDURE DIVISION.
000000*----------Initialize-------------
000000 MOVE SPACE TO CHR.
000000*---------------------------------


000000*---------Input by user-----------
000000 ACCEPT TEMP.
000000 IF TEMP = "GPS" THEN
             DISPLAY "Welcom GPS"
000000 ELSE
             DISPLAY "Please type GPS"
000000 END-IF.
000000*---------------------------------


000000*-----Initialize(additional)------
000000* INITIALIZE statement resets the values of all subordinate data
000000* num -> zero, char -> space

000000 INITIALIZE STR.
000000*---------------------------------
