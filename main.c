#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void text_to_speech(const char* text) {
    char command[256];
    snprintf(command, sizeof(command), "espeak \"%s\"", text);
    system(command);
}

int main() {
    char text[256];
    printf("Masukkan teks yang ingin diubah menjadi suara: ");
    fgets(text, sizeof(text), stdin);

    // Hapus karakter newline dari input fgets
    size_t len = strlen(text);
    if (len > 0 && text[len-1] == '\n') {
        text[len-1] = '\0';
    }

    text_to_speech(text);
    return 0;
}
