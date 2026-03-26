// Lesson Reference -> https://www.boot.dev/lessons/d3fe56ab-a7bf-4847-9fd7-299f1fe5fe03


void concat_strings(char *str1, const char *str2) {

  // loop to find "\0" in str1

  if (*str1 == '\0' && *str2 == '\0'){
    return;
  }

  while (*str1 != '\0'){
    str1 ++;
  }

  while (*str2 != '\0'){
    *str1 = *str2;
    str1 ++;
    str2 ++;
  }
  
  *str1 = '\0'; 

}