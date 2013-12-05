#include <stdio.h>
#include <time.h>

int main()
{
	clock_t begin, end;
	double timeSpent;
	FILE *fp;
	fp = fopen("bs", "w");
	
	int max = 50000000;
	int count = 0;
	begin = clock();
	
	while(count <= max){
		fprintf(fp, "bullshit\n");
		count++;
	}
	end = clock();
	timeSpent = (double)(end - begin) / CLOCKS_PER_SEC;

	fclose(fp);
	
	printf("time spent=%d", timeSpent);
	return 0;
}
