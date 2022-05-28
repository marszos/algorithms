def list_to_ll(lista):
    d = dict(lista)
    node_path2 = []
    
    
    for link in d.keys() - d.values():
        node_path1 = [link]
        
        while link in d:
            link = d[link]
            node_path1.append(link)
        
        node_path2.append(node_path1)
    
    return node_path2[0][-1]
  
  
  
  
  def destination_city(paths):
    count_cities = {}
    
    for path in paths:
        city_a, city_b = path 
        count_cities[city_a] = count_cities.get(city_a, 0) + 1
        count_cities[city_b] = count_cities.get(city_b, 0)
        
    
    for city in count_cities:
        if count_cities[city] == 0:
            return city
          
          
          
   paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
  
  # https://leetcode.com/problems/destination-city/submissions/
