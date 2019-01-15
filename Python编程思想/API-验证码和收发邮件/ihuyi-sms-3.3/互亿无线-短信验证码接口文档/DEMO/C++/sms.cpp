//�ӿ����ͣ��������ߴ������Žӿڣ�֧�ַ�����֤����š�����֪ͨ���ŵȡ�
// �˻�ע�᣺��ͨ���õ�ַ��ͨ�˻�http://sms.ihuyi.com/register.html
// ע�����
//��1�������ڼ䣬����Ĭ�ϵ�ģ����в��ԣ�Ĭ��ģ������ӿ��ĵ���
//��2����ʹ��APIID���鿴APIID���¼�û�����->��֤�����->��Ʒ����->APIID���� APIkey�����ýӿڣ�
//��3���ô���������뻥�����߶��Žӿڲο�ʹ�ã��ͻ��ɸ���ʵ����Ҫ���б�д��

// DEMO�����ο�
#include <arpa/inet.h>
#include <assert.h>
#include <errno.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <netdb.h>
#include <unistd.h>

#define SA struct sockaddr
#define MAXLINE 4096
#define MAXSUB  2000
#define MAXPARAM 2048
#define LISTENQ 1024

extern int h_errno;

int basefd;
char *hostname = "106.ihuyi.cn";
char *send_sms_uri = "/webservice/sms.php?method=Submit&format=json";

/**
* ��http post����
*/
ssize_t http_post(char *page, char *poststr)
{
    char sendline[MAXLINE + 1], recvline[MAXLINE + 1];
    ssize_t n;
    snprintf(sendline, MAXSUB,
        "POST %s HTTP/1.0\r\n"
        "Host: %s\r\n"
        "Content-type: application/x-www-form-urlencoded\r\n"
        "Content-length: %zu\r\n\r\n"
        "%s", page, hostname, strlen(poststr), poststr);

    write(basefd, sendline, strlen(sendline));
    while ((n = read(basefd, recvline, MAXLINE)) > 0) {
        recvline[n] = '\0';
        printf("%s", recvline);
    }
    return n;
}

/**
* ���Ͷ���
*/
ssize_t send_sms(char *account, char *password, char *mobile, char *content)
{
    char params[MAXPARAM + 1];
    char *cp = params;
    sprintf(cp,"account=%s&password=%s&mobile=%s&content=%s", account, password, mobile, content);
    return http_post(send_sms_uri, cp);
}

int  socked_connect(char *arg)
{
    struct sockaddr_in their_addr = {0};  
    char buf[1024] = {0};  
    char rbuf[1024] = {0};  
    char pass[128] = {0};  
    struct hostent *host = NULL;   
    
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd<0)
    {
        printf ("create the sockfd is failed\n");
        return -1;
    }
    
    if((host = gethostbyname(arg))==NULL)  
    {  
        printf("Gethostname error, %s\n");  
        return -1; 
    }  
 
    memset(&their_addr, 0, sizeof(their_addr));  
    their_addr.sin_family = AF_INET;  
    their_addr.sin_port = htons(80);  
    their_addr.sin_addr = *((struct in_addr *)host->h_addr);
    if(connect(sockfd,(struct sockaddr *)&their_addr, sizeof(struct sockaddr)) < 0)  
    {  
        close(sockfd);
        return  -1;
    }  
    printf ("connect is success\n");
    return sockfd;
    
}

int main(void)
{
    struct sockaddr_in servaddr;
    char str[50];
    
    #if 0
    //����socket����
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_addr =*(hostname);
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(80);
    inet_pton(AF_INET, str, &servaddr.sin_addr);
    connect(sockfd, (SA *) & servaddr, sizeof(servaddr));
    #endif
    
    if((basefd= socked_connect(hostname))==-1)
    {
        printf("connect is failed\n");
        return -1;
    }
    printf("basefd is =%d\n",basefd);
    //�û����ǵ�¼�û�����->��֤�����->��Ʒ����->APIID
    char *account = "�û���";

    //�鿴�������¼�û�����->��֤�����->��Ʒ����->APIKEY
    char *password = "����";

    //�ֻ���
    char *mobile = "138xxxxxxxx";

    //��������
    char *message = "���ã�������֤����123456";

    /**************** ���Ͷ��� *****************/
    send_sms(account, password, mobile, message);
    printf("send the message is success\n");
    close(basefd);
    exit(0);
}