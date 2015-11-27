#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define N 100
 
void pp(char v[][20])
{
  int             i;
  puts("---------------");
  for (i = 0; *v[i]; i++)
    printf("%s, ", v[i]);
  puts("\n---------------");
}
 
double calc(char *s)
{
  char           *w = malloc(N), *p, *p2, v[N][20];
  int             i, diff;
  double          acc;
 
  /* ()calc */
  while ((p = strchr(s, ')'))) {
    p2 = p + 1;
    *p = '\0';
    while (*p != '(')
      p--;
    *p = '\0';
    sprintf(w, "%s %g %s", s, calc(p + 1), p2);
    sprintf(s, "%s", w);
  }
 
  /* tokenize */
  i = 0;
  sscanf(s, "%s", v[i]);
  p = strtok(s, " ");
  while (p) {
    sprintf(v[i], "%s", p);
    p = strtok(NULL, " ");
    i++;
  }
  sprintf(v[i], "%s", "");
 
  /* log calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("log", v[i]) == 0) {
      sprintf(v[i], "%g", log10(atof(v[i + 1])));
      sprintf(v[i + 1], " ");
    }
  }
 
  /* sin calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("sin", v[i]) == 0) {
      sprintf(v[i], "%g", sin(atof(v[i + 1]) / 180 * M_PI));
      sprintf(v[i + 1], " ");
    }
  }
 
  /* cos calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("cos", v[i]) == 0) {
      sprintf(v[i], "%g", cos(atof(v[i + 1]) / 180 * M_PI));
      sprintf(v[i + 1], " ");
    }
  }
 
  /* tan calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("tan", v[i]) == 0) {
      sprintf(v[i], "%g", tan(atof(v[i + 1]) / 180 * M_PI));
      sprintf(v[i + 1], " ");
    }
  }
 
  /* compact */
  diff = 0;
  for (i = 0; *v[i]; i++) {
    if (*v[i] == ' ')
      diff++;
    if (diff && *v[i] != ' ')
      sprintf(v[i - diff], "%s", v[i]);
  }
  sprintf(v[i - diff], "%s", "");
 
  /* - calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("-", v[i]) == 0) {
      sprintf(v[i], "+");
      sprintf(v[i + 1], "%g", -atof(v[i + 1]));
    }
  }
 
  /* / calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("/", v[i]) == 0) {
      sprintf(v[i], "*");
      sprintf(v[i + 1], "%g", 1 / atof(v[i + 1]));
    }
  }
 
  /* * calc */
  for (i = 0; *v[i]; i++) {
    if (strcmp("*", v[i]) == 0) {
      sprintf(v[i], " ");
      sprintf(v[i + 1], "%g", atof(v[i - 1]) * atof(v[i + 1]));
      sprintf(v[i - 1], "0");
    }
  }
 
  /* pp(v); */
 
  /* + calc */
  acc = 0;
  for (i = 0; *v[i]; i++)
    acc += atof(v[i]);
  return acc;
}
 
char *insertBlank(char *s)
{
  char           *w = malloc(N);
 
  *w = '\0';
  while (*s) {
    if (strchr("+-*/()", *s)) {
      strcat(w, " ");
      strncat(w, s, 1);
      strcat(w, " ");
    } else {
      strncat(w, s, 1);
    }
    s++;
  }
 
  return w;
}
 
 
double dentaku(char *s)
{
  return calc(insertBlank(s));
}
 
int main(int argc,char**argv) {
 
  char           *s[] = {
    "2  +  5  /  5  +  4   *   2   +   1",
    "2 * 3 + 1",
    "( 2 + 3 ) * 7 * ( 3 - 1 )",
    "sin(90) * 2 + 1 - 2",
    "log(3) * 2 + 1",
    "1-2*(3+1)-2",
    "log(log(123))",
    "log log 123",
    "1+(  log(2 *sin (5*log (2)+1)/2)+3*4)"
  };
  int i;
  for (i = 0; i<9; i++)
    printf("input = %s\nresult = %g\n\n", s[i], dentaku(s[i]));
 
  return 0;
}
