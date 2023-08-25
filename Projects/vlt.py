'''Criar programa que leia a solicitação do usuário e mostre a grade de horários completa, grade de apenas uma estação
ou a duração de uma viagem da estação X para estação Y(primeiro projeto utilizando apenas estrutura condicional!)'''

from time import sleep
import cv2

#DEFININDO A SOLICITAÇÃO DO USUÁRIO

while True:
    print("\n======HORÁRIOS VLT======\n\n")
    print("Escolha a opção que deseja utilizar:\n[1] GRADE DE HORÁRIOS COMPLETA\n[2] GRADE DE HORÁRIOS DE UMA ESTAÇÃO\n[3] SAIR DO PROGRAMA")
    user=int(input("Sua escolha: "))
    if user==3:
        print("\nObrigado por usar nosso aplicativo!")
        sleep(1)
        break
    
#CASO PRIMEIRA OPÇÃO SEJA ESCOLHIDA
    if user==1:
        print("\n\nEscolha a grade de horário de qual sentido deseja ver:\n[1] SENTIDO IATE\n[2] SENTIDO PARANGABA\n[3] VOLTAR")
        sentido=int(input("Sua escolha: "))
        print("PROCESSANDO\n")
        sleep(0.5)
        if sentido==1:
            img1=cv2.imread('imagens/sentido_iate.jpg')
            cv2.imshow('sentido_iate.jpg', img1)
            cv2.waitKey(0)
            cv2.destroyWindow()
            print('\n\n')
        elif sentido==2:
            img2=cv2.imread('imagens/sentido_parangaba.jpg')
            cv2.imshow('sentido_parangaba.jpg', img2)
            cv2.waitKey(0)
            cv2.destroyWindow()
            print('\n\n')


#CASO SEGUDA OPÇÃO SEJA ESCOLHIDA
    elif user==2:
        print('\n\n')
        print("Escolha a grade de horário de qual sentido deseja ver:\n[1] SENTIDO IATE\n[2] SENTIDO PARANGABA\n[3] VOLTAR")
        sentido=int(input("Sua escolha: "))


    #SENTIDO IATE
        while sentido==1:
                print("\n\n====== SENTIDO IATE ======\n")
                print("Escolha a estação que deseja ver a grade de horários: ")
                print("[1] PARANGABA           [7] PONTES VIEIRA\n[2] MONTESE             [8] ANTÔNIO SALES\n[3] EXPEDICIONÁRIOS     [9] PAPICU\n[4] VILA UNIÃO          [10] MUCURIPE\n[5] B. DE MELO          [11] IATE\n[6] S.J. DO TAUAPE      [12] VOLTAR")
                estac=int(input("Sua escolha: "))
                if estac==1:
                    print("\nESTAÇÃO PARANGABA\n")
                    print("5:30 | 6:08 | 6:46 | 7:26 | 8:06 | 8:47 | 9:28 | 10:09 | 10:50 | 11:30 | 12:10 | 12:50 | 13:30 | 14:10")
                    print("14:50 | 15:30 | 16:10 | 16:50 | 17:30 | 18:10 | 18:50 | 19:28 | 20:06 | 20:44 | 21:21 | 21:58 | 22:35\n\n")
                    sleep(3)

                elif estac==2:
                    print("\nESTAÇÃO MONTESE\n")
                    print("5:33 | 6:11 | 6:49 | 7:29 | 8:09 | 8:50 | 9:31 | 10:12 | 10:53 | 11:33 | 12:13 | 12:53 | 13:33")
                    print("14:13| 15:33 | 16:13 | 16:53 | 17:33 | 18:13 | 18:53 | 19:31 | 20:09 | 20:47 | 21:24 | 22:01 | 22:38\n\n")
                    sleep(3)

                elif estac==3:
                    print("\nESTAÇÃO EXPEDICIONÁRIOS\n")
                    print("5:35 | 6:13 | 6:51 | 7:32 | 8:12 | 8:53 | 9:34 | 10:15 | 10:56 | 11:36 | 12:16 | 12:56 | 13:36 | 14:16")
                    print("14:56 | 15:36 | 16:16 | 16:56 | 17:36 | 18:16 | 18:56 | 19:33 | 20:11 | 20:49 | 21:26 | 22:03 | 22:40\n\n")
                    sleep(3)

                elif estac==4:
                    print("\nESTAÇÃO VILA UNIÃO\n")
                    print("5:38 | 6:16 | 6:54 | 7:36 | 8:16 | 8:57 | 9:38 | 10:18 | 10:59 | 11:39 | 12:19 | 12:59 | 13:39 | 14:19")
                    print("14:59 | 15:39 | 16:19 | 16:59 | 17:39 | 18:19 | 18:59 | 19:36 | 20:14 | 20:52 | 21:28 | 22:05 | 22:42\n\n")
                    sleep(3)

                elif estac==5:
                    print("\nESTAÇÃO B. DE MELO\n")
                    print("5:42 | 6:20 | 6:58 | 7:40 | 8:20 | 9:01 | 10:22 | 11:03 | 11:43 | 12:23 | 13:03 | 13:43 | 13:23 | 15:03")
                    print("15:43 | 16:23 | 17:03 | 17:43 | 18:23 | 19:03 | 19:40 | 20:18 | 20:56 | 21:32 | 22:09 | 22:46\n\n")
                    sleep(3)

                elif estac==6:
                    print("\nESTAÇÃO S.J. DO TAUAPE\n")
                    print("5:46 | 6:24 | 7:02 | 7:44 | 8:24 | 9:05 | 9:46 | 10:26 | 11:07 | 11:47 | 12:27 | 13:07 | 13:47 | 14:27")
                    print("15:07 | 15:47 | 16:27 | 17:07 | 17:47 | 18:27 | 19:07 | 19:44 | 20:22 | 21:00 | 21:36 | 22:13 | 22:50\n\n")
                    sleep(3)

                elif estac==7:
                    print("\nESTAÇÃO PONTES VIEIRA\n")
                    print("5:51 | 6:29 | 7:07 | 7:49 | 8:29 | 9:10 | 9:51 | 10:31 | 11:12 | 11:52 | 12:32 | 13:12 | 13:52 | 14:32")
                    print("15:12 | 15:52 | 16:32 | 17:12 | 17:52 | 18:32 | 19:12 | 19:49 | 20:27 | 21:05 | 21:41 | 22:18 | 22:55\n\n")
                    sleep(3)

                elif estac==8:
                    print("\nESTAÇÃO ANTÔNIO SALES\n")
                    print("5:54 | 6:32 | 7:10 | 7:52 | 8:32 | 9:13 | 9:54 | 10:34 | 11:15 | 11:55 | 12:35 | 13:15 | 13:55 | 14:35")
                    print("15:15 | 15:55 | 16:35 | 17:15 | 17:55 | 18:35 | 19:15 | 19:52 | 20:30 | 21:08 | 21:44 | 22:21 | 22:58\n\n")
                    sleep(3)

                elif estac==9:
                    print("\nESTAÇÃO PAPICU\n")
                    print("5:58 | 6:36 | 7:14 | 7:56 | 8:36 | 9:17 | 9:58 | 10:38 | 11:19 | 11:59 | 12:39 | 13:19 | 13:59 | 14:39")
                    print("15:19 | 15:59 | 16:39 | 17:19 | 17:59 | 18:39 | 19:19 | 19:56 | 20:34 | 21:12 | 21:48 | 22:25 | 23:02\n\n")
                    sleep(3)

                elif estac==10:
                    print("\nESTAÇÃO MUCURIPE\n")
                    print("6:02 | 6:40 | 7:18 | 8:00 | 8:40 | 9:21 | 10:02 | 10:42 | 11:23 | 12:03 | 12:43 | 13:23 | 14:03 | 14:43")
                    print("15:23 | 16:03 | 16:43 | 17:23 | 18:03 | 18:43 | 19:23 | 20:00 | 20:38 | 21:16 | 21:52 | 22:29 | 23:06\n\n")
                    sleep(3)

                elif estac==11:
                    print("\nESTAÇÃO IATE\n")
                    print("6:05 | 6:43 | 7:21 | 8:03 | 8:43 | 9:24 | 10:05 | 10:45 | 11:26 | 12:46 | 13:26 | 14:06 | 14:46 | 15:26")
                    print("16:06 | 16:46 | 17:26 | 18:06 | 18:46 | 19:26 | 20:03 | 20:41 | 21:19 | 21:55 | 22:32 | 23:09 \n\n")
                    sleep(3)

                elif estac ==12:
                    sleep(0.5)
                    break
            
                    
                
    #SENTIDO PARANGABA
        while sentido==2:
                print("\n\n====== SENTIDO PARANGABA ======\n")
                print("Escolha a estação que deseja ver a grade de horários: ")
                print("[1] IATE               [7] B. DE MELO\n[2] MONTESE            [8] VILA UNIÃO\n[3] PAPICU             [9] EXPEDICIONÁRIOS\n[4] ANTÔNIO SALES      [10] MONTESE\n[5] PONTES VIEIRA      [11] PARANGABA \n[6] S.J. DO TAUAPE     [12] VOLTAR")
                estac=int(input("Sua escolha: "))

                if estac==1:
                    print("\nESTAÇÃO IATE\n")
                    print("5:30 | 6:08 | 6:46 | 7:26 | 8:06 | 8:47 | 9:28 | 10:09 | 10:50 | 11:30 | 12:10 | 12:50 | 13:30 | 14:10")
                    print("14:50 | 15:30 | 16:10 | 16:50 | 17:30 | 18:10 | 18:50 | 19:28 | 20:06 | 20:44 | 21:21 | 21:58 | 22:35\n\n")
                    sleep(3)

                elif estac==2:
                    print("\nESTAÇÃO MUCURIPE\n")
                    print("5:33 | 6:11 | 6:49 | 7:29 | 8:09 | 8:50 | 9:31 | 10:12 | 10:53 | 11:33 | 12:13 | 12:53 | 13:33")
                    print("14:13| 15:33 | 16:13 | 16:53 | 17:33 | 18:13 | 18:53 | 19:31 | 20:09 | 20:47 | 21:24 | 22:01 | 22:38\n\n")
                    sleep(3)

                elif estac==3:
                    print("\nESTAÇÃO PAPICU\n")
                    print("5:37 | 6:15 | 6:53 | 7:33 | 8:13 | 8:54 | 9:35 | 10:16 | 10:57 | 11:37 | 12:17 | 12:57 | 13:37 | 14:17")
                    print("14:57 | 15:37 | 16:17 | 16:57 | 17:37 | 18:17 | 18:57 | 19:35 | 20:13 | 20:51 | 21:28 | 22:05 | 22:42\n\n")
                    sleep(3)

                elif estac==4:
                    print("\nESTAÇÃO ANTÔNIO SALES\n")
                    print("5:41 | 6:19 | 6:57 | 7:37 | 8:17 | 8:58 | 9:39 | 10:20 | 11:01 | 11:41 | 12:21 | 13:01 | 13:41 | 14:21")
                    print("15:01 | 15:41 | 16:21 | 17:01 | 17:41 | 18:21 | 19:01 | 19:39 | 20:17 | 20:55 | 21:32 | 22:09 | 22:46\n\n")
                    sleep(3)

                elif estac==5:
                    print("\nESTAÇÃO PONTES VIEIRA\n")
                    print("5:44 | 6:22 | 7:00 | 7:40 | 8:20 | 9:01 | 9:42 | 10:23 | 11:04 | 11:44 | 12:24 | 13:04 | 13:44 | 13:24")
                    print("15:04 | 15:44 | 16:24 | 17:04 | 17:44 | 18:24 | 19:04 | 19:42 | 20:20 | 20:58 | 21:35 | 22:12 | 22:49\n\n")
                    sleep(3)
                    
                elif estac==6:
                    print("\nESTAÇÃO S.J. DO TAUAPE\n")
                    print("5:49 | 6:27 | 7:05 | 7:45 | 8:25 | 9:05 | 9:47 | 10:28 | 11:09 | 11:49 | 12:29 | 13:09 | 13:49 | 14:29")
                    print("15:09 | 15:49 | 16:29 | 17:09 | 17:49 | 18:29 | 19:09 | 19:47 | 20:25 | 21:03 | 21:39 | 22:16 | 22:53\n\n")
                    sleep(3)

                elif estac==7:
                    print("\nESTAÇÃO B. DE MELO\n")
                    print("5:53 | 6:31 | 7:09 | 7:49 | 8:29 | 9:10 | 9:51 | 10:32 | 11:13 | 11:53 | 12:33 | 13:13 | 13:53 | 14:33")
                    print("15:12 | 15:53 | 16:33 | 17:13 | 17:53 | 18:33 | 19:13 | 19:51 | 20:29 | 21:07 | 21:44 | 22:21 | 22:58\n\n")
                    sleep(3)

                elif estac==8:
                    print("\nESTAÇÃO VILA UNIÃO\n")
                    print("5:57 | 6:35 | 7:13 | 7:53 | 8:33 | 9:14 | 9:55 | 10:36 | 11:17 | 11:57 | 12:37 | 13:17 | 13:57 | 14:37")
                    print("15:15 | 15:57 | 16:37 | 17:17 | 17:57 | 18:37 | 19:17 | 19:55 | 20:33 | 21:11 | 21:48 | 22:25 | 23:02\n\n")
                    sleep(3)

                elif estac==9:
                    print("\nESTAÇÃO EXPEDICIONÁRIOS\n")
                    print("6:00 | 6:38 | 7:16 | 7:57 | 8:37 | 9:18 | 9:59 | 10:39 | 11:20 | 12:00 | 12:40 | 13:20 | 14:00 | 14:40")
                    print("15:19 | 16:00 | 16:40 | 17:20 | 18:00 | 18:40 | 19:20 | 19:58 | 20:36 | 21:14 | 21:50 | 22:27 | 23:04\n\n")
                    sleep(3)
                
                elif estac==10:
                    print("\nESTAÇÃO MONTESE\n")
                    print("6:02 | 6:40 | 7:18 | 8:00 | 8:40 | 9:21 | 10:02 | 10:42 | 11:23 | 12:03 | 12:43 | 13:23 | 14:03 | 14:43")
                    print("15:23 | 16:03 | 16:43 | 17:23 | 18:03 | 18:43 | 19:23 | 20:00 | 20:38 | 21:16 | 21:52 | 22:29 | 23:06\n\n")
                    sleep(3)
                
                elif estac==11:
                    print("\nESTAÇÃO PARANGABA\n")
                    print("6:05 | 6:43 | 7:21 | 8:03 | 8:43 | 9:24 | 10:05 | 10:45 | 11:26 | 12:46 | 13:26 | 14:06 | 14:46 | 15:26")
                    print("16:06 | 16:46 | 17:26 | 18:06 | 18:46 | 19:26 | 20:03 | 20:41 | 21:19 | 21:55 | 22:32 | 23:09 \n\n")
                    sleep(3)
               
                elif estac==12:
                    sleep(0.5)
                    break