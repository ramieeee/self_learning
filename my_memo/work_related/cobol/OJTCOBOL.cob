000000 IDENTIFICATION DIVISION.
000000 PROGRAM-ID.    OJTCOBOL.
000000 ENVIRONMENT DIVISION.
000000 INPUT-OUTPUT SECTION.
000000 FILE-CONTROL.
000000     SELECT OJTKSDATA ASSIGN TO RAMIEOJT
000000     ORGANIZATION IS INDEXED
000000*     ACCESS MODE IS DYNAMIC
000000     RECORD KEY IS KEY-VAL.
000000 DATA DIVISION.
000000 FILE SECTION.
000000 FD OJTKSDATA.
000000     01 IN-DATA.
000000         03 KEY-VAL               PIC 9(3).
000000         03 SAY-HELLO-WORLD       PIC X(13).
000000 WORKING-STORAGE SECTION.
000000     01 EXIT-CODE                 PIC 9(1) VALUE 0.
000000     01 TEMP-KEY                  PIC 9(3).
000000
000000 PROCEDURE DIVISION.
000000*     ACCEPT KEY-VAL.
000000     MOVE "001" TO KEY-VAL.
000000     DISPLAY "***BATCH TEST_RAMHEE YEON***".
000000     OPEN INPUT OJTKSDATA.
000000     START OJTKSDATA KEY EQUAL KEY-VAL
000000*     START OJTKSDATA KEY EQUAL TEMP-KEY
000000         INVALID KEY 
000000             DISPLAY 'INVALID KEY'
000000         NOT INVALID KEY
000000             PERFORM READ-NEXT
000000     END-START.
000000     CLOSE OJTKSDATA.
000000     DISPLAY "***END***".
000000     STOP RUN.
000000 
000000 READ-NEXT.
000000     PERFORM UNTIL EXIT-CODE=1
000000         READ OJTKSDATA
000000             AT END MOVE 1 TO EXIT-CODE
000000             NOT AT END
000000                 DISPLAY IN-DATA
000000     END-PERFORM.
