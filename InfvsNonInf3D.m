total=input('What is the square root of population size? ');
population= zeros(total,total,3);
sus=[0 0 1];
recov=[0 1 0];
status=[sus];
for i=1:total
    for j=1:total
        choosestatus=status(ceil(rand),:);
        for k=1:3
             population(i,j,k)=choosestatus(k);
        end
    end
end
sick=input('How many infected to start with? ');
inf=[1 0 0];
counter=0;
while counter<sick
    randomR=ceil(total*rand);
    randomC=ceil(total*rand);
    if find(population(randomR,randomC, :))~=find(inf);
        for fill=1:3
            population(randomR,randomC,fill)=inf(fill);
        end
        counter=counter+1;
    end
end
period=input('what [InfectionPeriod InfectionProbability RecoveryPeriod MigrationFrequency]? ');
SimuPeriod=input('How long the simulation would last for? ');
%rules
simulation=zeros(total,total,3,SimuPeriod);
simulation(:,:,:,1)=population(:,:,:);
sickness=zeros(total,total);
recovery=zeros(total,total);
for ro=1:total
    for co=1:total
        if (find(simulation(ro,co,:,1)))==1
            sickness(ro,co)=1;
        else sickness(ro,co)=0;
        end
        if (find(simulation(ro,co,:,1)))==2
            recovery(ro,co)=1;
        else recovery(ro,co)=0;
        end
    end
end
    
for time=2:SimuPeriod
    for rows=1:total
        for columns=1:total
            if find(simulation(rows,columns,:,time-1))==1 & sickness(rows,columns)<period(1)
                simulation(rows,columns,:,time)=[1 0 0];
                sickness(rows,columns)=sickness(rows,columns)+1;
                recovery(rows,columns)=0;
            elseif find(simulation(rows,columns,:,time-1))==1 & sickness(rows,columns)==period(1)
                simulation(rows,columns,:,time)=[0 1 0];
                sickness(rows,columns)=0;
                recovery(rows,columns)=1;
            end
            if find(simulation(rows,columns,:,time-1))==2 & recovery(rows,columns)<period(3)
                simulation(rows,columns,:,time)=[0 1 0];
                recovery(rows, columns)=recovery(rows,columns)+1;
                sickness(rows,columns)=0;
            elseif find(simulation(rows,columns,:,time-1))==2 & recovery(rows,columns)==period(3)
                simulation(rows,columns,:,time)=[0 0 1];
                recovery(rows,columns)=0;
                sickness(rows,columns)=0;
            end
            if find(simulation(rows,columns,:,time-1))==3 
                if rows==1 & columns==1
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows,columns+1,1,time-1))))==1
                           simulation(rows,columns,:,time)=[1 0 0];
                           sickness(rows,columns)=1;
                           recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows==1 & columns==total
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows,columns-1,1,time-1))))==1
                           simulation(rows,columns,:,time)=[1 0 0];
                           sickness(rows,columns)=1;
                           recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows==1 & columns>1 & columns<total
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows,columns-1,1,time-1)+simulation(rows,columns+1,1,time-1))))==1
                           simulation(rows,columns,:,time)=[1 0 0];
                           sickness(rows,columns)=1;
                           recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows>1 & rows<total & columns==1
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows-1,columns,1,time-1)+simulation(rows,columns+1,1,time-1))))==1
                          simulation(rows,columns,:,time)=[1 0 0];
                          sickness(rows,columns)=1;
                          recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows>1 & rows<total & columns==total
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows-1,columns,1,time-1)+simulation(rows,columns-1,1,time-1))))==1
                        simulation(rows,columns,:,time)=[1 0 0];
                        sickness(rows,columns)=1;
                        recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows==total & columns==1
                    if find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows-1,columns,1,time-1)+simulation(rows,columns+1,1,time-1))))==1 
                            simulation(rows,columns,:,time)=[1 0 0];
                            sickness(rows,columns)=1;
                            recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows==total & columns==total
                    if find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows-1,columns,1,time-1)+simulation(rows,columns-1,1,time-1))))==1
                           simulation(rows,columns,:,time)=[1 0 0];
                           sickness(rows,columns)=1;
                           recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                        sickness(rows,columns)=1;
                    end
                elseif rows==total & columns>1 & columns<total
                    if find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows-1,columns,1,time-1)+simulation(rows,columns+1,1,time-1)+simulation(rows,columns-1,1,time-1))))==1
                        simulation(rows,columns,:,time)=[1 0 0];
                        sickness(rows,columns)=1;
                        recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else
                        simulation(rows,columns,:,time)=[0 0 1];
                    end
                elseif rows>1 & rows<total & columns>1 & columns<total
                    if find(simulation(rows+1,columns,:,time-1))==1 | find(simulation(rows-1,columns,:,time-1))==1 | find(simulation(rows,columns+1,:,time-1))==1 | find(simulation(rows,columns-1,:,time-1))==1 
                        if round(1-(1-period(2))^(sum(simulation(rows+1,columns,1,time-1)+simulation(rows-1,columns,1,time-1)+simulation(rows,columns+1,1,time-1)+simulation(rows,columns-1,1,time-1))))==1
                           simulation(rows,columns,:,time)=[1 0 0];
                           sickness(rows,columns)=1;
                           recovery(rows,columns)=0;
                        else
                            simulation(rows,columns,:,time)=[0 0 1];
                        end
                    else 
                        simulation(rows,columns,:,time)=[0 0 1];
                        
                    end
                end
            end
        end
            if rows==total & columns==total
               mig=0;
               while mig<period(4)
                     ro=ceil(total*rand);
                     col=ceil(total*rand);
                     if ro<total & col<total
                        migration=simulation(rows, columns,:,time);
                        simulation(rows,columns,:,time)=simulation(ro,col,:,time);
                        simulation(ro,col,:,time)=migration;
                        mig=mig+1;
                     end
               end   
            end 
    end
end
for i=1:SimuPeriod
    image(simulation(:,:,:,i));
    pause(0.5);
end
graph=zeros(SimuPeriod,3);
for time=1:SimuPeriod
    sick=0;
    recovery=0;
    sus=0;
    for rows=1:total
        for columns=1:total
            if find(simulation(rows,columns,:,time))==1
                sick=sick+1;
            elseif find(simulation(rows,columns,:,time))==2
                recovery=recovery+1;
            elseif find(simulation(rows,columns,:,time))==3
                sus=sus+1;
            end
        end
    end
    graph(time,1)=time;
    graph(time,2)=sick;
    graph(time,3)=recovery+sus;
end

plot3(graph(:,3),graph(:,2),graph(:,1));
ylabel('Infected'), xlabel('Uninfected'), zlabel('Time')


                
            