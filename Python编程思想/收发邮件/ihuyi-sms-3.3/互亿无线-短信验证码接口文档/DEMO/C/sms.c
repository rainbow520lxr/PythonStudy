//�ӿ����ͣ��������ߴ������Žӿڣ�֧�ַ�����֤����š�����֪ͨ���ŵȡ�
//�˻�ע�᣺��ͨ���õ�ַ��ͨ�˻�http://sms.ihuyi.com/register.html
//ע�����
//��1�������ڼ䣬����Ĭ�ϵ�ģ����в��ԣ�Ĭ��ģ������ӿ��ĵ���
//��2����ʹ��APIID���鿴APIID���¼�û�����->��֤�����->��Ʒ����->APIID����APIkey�����ýӿڣ�
//��3���ô���������뻥�����߶��Žӿڲο�ʹ�ã��ͻ��ɸ���ʵ����Ҫ���б�д��

#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h>
#include <errno.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <netinet/in.h>
#include <arpa/inet.h>
 
#define IPSTR "106.ihuyi.cn"
#define PORT 80
#define BUFSIZE 1024

 
//�������� 2015-07-27
//linux�µı��뷽�� gcc -o sms sms.c

int main(int argc, char **argv)
{
        int sockfd, ret, i, h,srandnum;
        struct sockaddr_in servaddr;
        char str1[4096], str2[4096], buf[BUFSIZE], *str;
        socklen_t len;
        fd_set   t_set1;
        struct timeval  tv;
 
        if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) {
                printf("������������ʧ��,���̼߳�����ֹ---socket error!\n");
                exit(0);
        };
 
        bzero(&servaddr, sizeof(servaddr));
        servaddr.sin_family = AF_INET;
        servaddr.sin_port = htons(PORT);
        if (inet_pton(AF_INET, IPSTR, &servaddr.sin_addr) <= 0 ){
                printf("������������ʧ��,���̼߳�����ֹ--inet_pton error!\n");
                exit(0);
        };
 
        if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0){
                printf("���ӵ�������ʧ��,connect error!\n");
                exit(0);
        }
        printf("��Զ�˽���������\n");
 
        //��������
		 //�û����ǵ�¼�û�����->��֤�����->��Ʒ����->APIID
          //�鿴�������¼�û�����->��֤�����->��Ʒ����->APIKEY
        memset(str2, 0, 4096);
        strcat(str2, "account=�û���&password=����&mobile=18930634151&content=������֤���ǣ�1212���벻Ҫ����֤��й¶�������ˡ�");
        str=(char *)malloc(128);
        len = strlen(str2);
        sprintf(str, "%d", len);
 
        memset(str1, 0, 4096);
        strcat(str1, "POST /webservice/sms.php?method=Submit&format=json HTTP/1.1\n");
        strcat(str1, "Host: 106.ihuyi.cn\n");
        strcat(str1, "Content-Type: application/x-www-form-urlencoded\n");
        strcat(str1, "Content-Length: ");
        strcat(str1, str);
        strcat(str1, "\n\n");
 
        strcat(str1, str2);
        strcat(str1, "\r\n\r\n");
        printf("%s\n",str1);
 
        ret = write(sockfd,str1,strlen(str1));
        if (ret < 0) {
                printf("����ʧ�ܣ����������%d��������Ϣ��'%s'\n",errno, strerror(errno));
                exit(0);
        }else{
                printf("��Ϣ���ͳɹ�����������%d���ֽڣ�\n\n", ret);
        }
 
        FD_ZERO(&t_set1);
        FD_SET(sockfd, &t_set1);
 
        while(1){
                sleep(2);
                tv.tv_sec= 0;
                tv.tv_usec= 0;
                h = 0;
                printf("--------------->1\r\n");
                h = select(sockfd +1, &t_set1, NULL, NULL, &tv);
                printf("--------------->2%d\r\n",h);
 
                //if (h == 0) continue;//break;


                if (h == 0) {
                        close(sockfd);
                        printf("���ӹرգ�\n");
                        return 1;
                };

                if (h < 0) {
                        close(sockfd);
                        printf("�ڶ�ȡ���ݱ���ʱSELECT��⵽�쳣�����쳣�����߳���ֹ��\n");
                        return -1;
                };
 
                if (h > 0){
                        memset(buf, 0, 4096);
                        i= read(sockfd, buf, 4095);
                        if (i==0){
                                close(sockfd);
                                printf("��ȡ���ݱ���ʱ����Զ�˹رգ����߳���ֹ��\n");
                                return -1;
                        }
 
                        printf("%s\n", buf);
                }
        }
        close(sockfd);
 
        return 0;
}