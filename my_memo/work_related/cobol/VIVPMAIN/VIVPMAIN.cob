       ID DIVISION.
       PROGRAM-ID.      VIVPMAIN.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       COPY VIVPM01.
       COPY VIVPFST.
      * COPY DFHAID.

       01 WS-FIRST-TIME-FLAG  PIC S9(4) COMP.
          88 FIRST-TIME                 VALUE 0.

       01 CALC-VALS.
           03 A PIC 9(2).
           03 B PIC 9(2).
           03 C PIC 9(4).

       01 WS-MSG PIC X(20).

       01 DEFINITIONS-OF-EIBAID-FIELD     PIC X(1).
          88 ENTER-KEY                              VALUE ''''.
          88 CLEAR-KEY                              VALUE '_'.
          88 PF1-KEY                                VALUE '1'.
          88 PF2-KEY                                VALUE '2'.
          88 PF3-KEY                                VALUE '3'.
          88 PF4-KEY                                VALUE '4'.
          88 PF5-KEY                                VALUE '5'.
          88 PF6-KEY                                VALUE '6'.
          88 PF7-KEY                                VALUE '7'.
          88 PF8-KEY                                VALUE '8'.
          88 PF9-KEY                                VALUE '9'.
          88 PF10-KEY                               VALUE ':'.
          88 PF11-KEY                               VALUE '#'.
          88 PF12-KEY                               VALUE '@'.

       01 START-CODE PIC X(2).

       01 WS-TRANS-ID       PIC X(4) VALUE 'VIVP'.
       01 WS-COMMUNICATION-AREA PIC X(1).

       PROCEDURE DIVISION.
      **** MAIN PROCEDURE ****
       0000-MAIN.
           PERFORM 5100-ALWAYS-TEST.

           EVALUATE TRUE

               WHEN FIRST-TIME
                   PERFORM 0100-FIRST-TIME

               WHEN ENTER-KEY
                   PERFORM 0001-RUN-PROG

               WHEN OTHER
                   PERFORM 9100-INVALID-KEY

           END-EVALUATE.

           PERFORM 5300-RETURN-TRANS-ID.

      **** PROGRAM RUN ****
       0001-RUN-PROG.
           PERFORM 0100-SEND-MAP.

           EXEC CICS HANDLE AID
                PF12(9999-ABORT)
                ANYKEY(9110-INVALID-KEY-RECEIVE-MAP)
                PF10
           END-EXEC.

           PERFORM 0200-RECEIVE-MAP.
           PERFORM 0300-CALC.
           PERFORM 0100-SEND-MAP.
           PERFORM 9999-ABORT.

      **** PROCEDURE LIST ****
       0100-FIRST-TIME.
           MOVE LOW-VALUES TO VIVPM01I.
           MOVE LOW-VALUES TO VIVPM01O.
           MOVE 'ENTER TWO NUMBERS' TO ALRTO.
           EXEC CICS SEND MAP('VIVPFST') MAPSET('VIVPFST')
               ERASE
           END-EXEC.

       0100-SEND-MAP.
           EXEC CICS SEND
               MAP('VIVPM01')
               MAPSET('VIVPM01')
               CURSOR
               ERASE
           END-EXEC.

       0200-RECEIVE-MAP.
           EXEC CICS RECEIVE
                MAP('VIVPM01')
                MAPSET('VIVPM01')
           END-EXEC.

       0300-CALC.
           MOVE NO1I TO A.
           MOVE NO2I TO B.
           COMPUTE C = A * B.
           MOVE C TO RSLTO.

       0400-SEND-MAP-DATA.
           EXEC CICS SEND
               MAP('VIVPM01')
               MAPSET('VIVPM01')
               FROM(VIVPM01O)
               DATAONLY
           END-EXEC.

       5100-ALWAYS-TEST.
           MOVE EIBAID TO DEFINITIONS-OF-EIBAID-FIELD.
           IF CLEAR-KEY
              PERFORM 9999-ABORT.

           EXEC CICS ASSIGN STARTCODE(START-CODE) END-EXEC.

           IF START-CODE  = 'TD' AND EIBCALEN NOT = 0 THEN
              MOVE 1 TO WS-FIRST-TIME-FLAG
           ELSE
              MOVE 0 TO WS-FIRST-TIME-FLAG
           END-IF.

       5300-RETURN-TRANS-ID.
            EXEC CICS
              RETURN TRANSID   (WS-TRANS-ID)
                     COMMAREA  (WS-COMMUNICATION-AREA)
                     LENGTH (LENGTH OF WS-COMMUNICATION-AREA)
            END-EXEC.

       9100-INVALID-KEY.
           MOVE LOW-VALUES TO VIVPM01O.
           MOVE 'INVALID KEY ENTERED' TO ALRTO.
           PERFORM 0400-SEND-MAP-DATA.

       9110-INVALID-KEY-RECEIVE-MAP.
           MOVE LOW-VALUES TO VIVPM01O.
           MOVE 'INVALID KEY ENTERED' TO ALRTO.
           PERFORM 0400-SEND-MAP-DATA.
           PERFORM 5300-RETURN-TRANS-ID.

       9999-ABORT.
           EXEC CICS RETURN
           END-EXEC.