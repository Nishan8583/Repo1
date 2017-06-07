			var imagecount = 1;
			var total = 5;
			function slide(x){
			
				var image = document.getElementById('img');
				imagecount = imagecount + x;
				if (imagecount > total){imagecount = 1;}
				if(imagecount < 1){imagecount = total;}
				image.src = "images/img" + imagecount + ".png";
				
				}
			
			window.setInterval(function slide(){
			
				var image = document.getElementById('img');
				imagecount = imagecount + 1;
				if (imagecount > total)
				{	
					imagecount = 1;
				}
				if(imagecount < 1)
				{
					imagecount = total;
				}
				image.src = "images/img" + imagecount + ".png";
			}
			,2000)
			
				
				
			
				function search()
				{
				var search1 = document.getElementById('search').value;
				window.open('https://www.google.com.np/search?q='+search1+'&oq='+search1+'&gs_l=serp.12...0.0.0.80.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.eSNfP-rFKjQ')
				}
				
				
				
					var count = 0;
					function newSite(x) {
					
					 count = count + x;
					var sites = ['https://www.youtube.com/embed/PWU-tjHllmY',
								'https://www.youtube.com/embed/tl39XPeb7UE',
								'https://www.youtube.com/embed/bKqeD7ojynw',
								'https://www.youtube.com/embed/fc_Mww4Ra5k',
								'https://www.youtube.com/embed/1NtFTpa6aCg',
								]
					if(count>4){count=0;}
					if(count<0){count=4;}
					document.getElementById('iframe').src = sites[count];
					}   
		
		
		
		
	