
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

void vycisti_buffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
        ;
}

// Zavolání funkce po každém scanf pro vyčištění bufferu, aby se zabránilo nekorektnímu chování programu při zadávání vstupu.
// vycisti_buffer();

void ukol1_trojuhelnik()
{
    int i;
    int x;

    for (i = 0; i <= 5; i++)
    {
        printf("\n");
        for (x = 0; i <= 10; i++)
        {
            printf("*");
        }
    }
}

void ukol2_ctverec()
{
}

void ukol3_pyramida()
{
}

void ukol4_caesar()
{
}

void ukol5_vigenere()
{
}

const char *ziskej_morse(char c)
{
    switch (c)
    {
    case 'A':
        return ".-";
    case 'B':
        return "-...";
    case 'C':
        return "-.-.";
    case 'D':
        return "-..";
    case 'E':
        return ".";
    case 'F':
        return "..-.";
    case 'G':
        return "--.";
    case 'H':
        return "....";
    case 'I':
        return "..";
    case 'J':
        return ".---";
    case 'K':
        return "-.-";
    case 'L':
        return ".-..";
    case 'M':
        return "--";
    case 'N':
        return "-.";
    case 'O':
        return "---";
    case 'P':
        return ".--.";
    case 'Q':
        return "--.-";
    case 'R':
        return ".-.";
    case 'S':
        return "...";
    case 'T':
        return "-";
    case 'U':
        return "..-";
    case 'V':
        return "...-";
    case 'W':
        return ".--";
    case 'X':
        return "-..-";
    case 'Y':
        return "-.--";
    case 'Z':
        return "--..";
    default:
        return "";
    }
}

void ukol6_morse()
{

    

}

int main()
{
    int volba;

    while (1)
    {
        printf("1 - Ukol 1: Pravouhly trojuhelnik\n");
        printf("2 - Ukol 2: Duty ctverec\n");
        printf("3 - Ukol 3: Rovnoramenna pyramida\n");
        printf("4 - Ukol 4: Caesarova sifra\n");
        printf("5 - Ukol 5: Vigenereova sifra\n");
        printf("6 - Ukol 6: Morseova abeceda\n");
        printf("0 - Ukoncit program\n");
        printf("Vyber ukol (0-6): ");

        if (scanf("%d", &volba) != 1)
        {
            printf("Neplatny vstup! Zadejte prosim cislo.\n");
            vycisti_buffer();
            continue;
        }
        vycisti_buffer();

        if (volba == 0)
        {
            printf("Ukoncuji program. Na shledanou!\n");
            break;
        }

        if (volba == 1)
            ukol1_trojuhelnik();
        else if (volba == 2)
            ukol2_ctverec();
        else if (volba == 3)
            ukol3_pyramida();
        else if (volba == 4)
            ukol4_caesar();
        else if (volba == 5)
            ukol5_vigenere();
        else if (volba == 6)
            ukol6_morse();
        else
        {
            printf("Neplatna volba! Vyberte cislo od 0 do 6.\n");
        }
    }

    return 0;
}
