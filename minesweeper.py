# create a grid
grid= [["#", "-", "-", "#", "-"],
       ["-", "#", "#", "-", "-"],
       ["-", "#", "-", "#", "#"],
       ["#", "-", "-", "-", "#"],
       ["#", "-", "#", "#", "-"]]    
# def function to count the number of #s at various positions around by iterating through rows and columns:
def minesweeper():
    for row in grid:
        index_row=grid.index(row)
        for col in row:
            index=row.index(col)
            count=0
            if col=="-":
                if index+1<len(row) and row[index+1]=="#":
                    count+=1
                if index-1>=0 and row[index-1]=="#":
                    count+=1
                if index_row+1<len(grid) and grid[index_row+1][index]=="#":
                    count+=1
                if index_row+1<len(grid) and index+1<len(row) and grid[index_row+1][index+1]=="#":
                    count+=1
                if index_row-1>=0 and index-1>=0 and grid[index_row-1][index-1]=="#":
                    count+=1
                if index_row-1>=0 and grid[index_row-1][index]=="#":
                    count+=1
                if index_row-1>=0 and index+1<len(row) and grid[index_row-1][index+1]=="#":
                    count+=1
                if index_row+1<len(grid) and index-1>=0 and grid[index_row+1][index-1]=="#":
                    count+=1    
                row[index]=count    

# call the function:
minesweeper()
for row in grid:
    print(row)

    

    
    
                
        
            

            
           
         
    

        
         


        

        
            
    

    

    
    


            
            
        
        
    

            
            
                

            
                

     
                


        


    



                        
                    
                
          
            


