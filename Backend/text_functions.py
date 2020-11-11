class textBuilder():
    def __init__( self ):
        self.carousel_count = 0
        return

    # Create an list with an array adapting it to a given channel
    def create_list( self, array, channel ):
        if channel == "web":
            result = "<ul>"
            for line in array:
                result = result + "<li>" + line + "</li>"
            result = result + "</ul>"
        if channel == "telephone":
            result = ""
            for line in array:
                result = result + "\n - " + line
            result = result + "\n"
        return result
    
    # Create html carousel with an array
    def create_carousel( self, itemsArray ):
        # Creates needed tags at the beginning of the carousel
        result = "<div id=\"carousel" + str(self.carousel_count) + "\" class=\"carousel slide\" data-ride=\"carousel\">"
        indicators = "<ol class=\"carousel-indicators\">"
        items = "<div class=\"carousel-inner\"> "
        count = 0
        
        for item in itemsArray:
            if count == 0:
                indicators = indicators + '<li data-target="#carousel' + str(self.carousel_count) + '" data-slide-to="0" class="active"></li>'
                items = items + """
                    <div class="carousel-item active">       
                    <img class="d-block w-100" src="https://source.unsplash.com/random/400x400" alt="
                """ + str(count) + """
                    slide"/>     
                    <div class="carousel-caption d-none d-md-block">
                        <h5>
                """ + item['name'] + """
                    </h5>
                    <p>
                """ + item['description'] + """
                    </div>
                    </div>
                """
            else:
                indicators = indicators + '<li data-target="#carousel' + str(self.carousel_count) + '" data-slide-to="' + str(count) + '" class="active"></li>'
                items = items + """
                    <div class="carousel-item">       
                    <img class="d-block w-100" src="https://source.unsplash.com/random/400x400" alt="
                """ + str(count) + """
                    slide"/>     
                    <div class="carousel-caption d-none d-md-block">
                        <h5>
                """ + item['name'] + """
                    </h5>
                    <p>
                """ + item['description'] + """
                    </div>
                    </div>
                """
            count = count + 1
        
        # Closes the tags added
        indicators = indicators + "</ol> " 
        items = items + "</div>"
        controls = """
            <a class="carousel-control-prev" href="#carousel""" + str(self.carousel_count) + """" role="button" data-slide="prev">     
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>     <span class="sr-only">Previous</span>  
            </a>   
            <a class="carousel-control-next" href="#carousel""" + str(self.carousel_count) + """" role="button" data-slide="next">     
                <span class="carousel-control-next-icon" aria-hidden="true"></span>     <span class="sr-only">Next</span>   
            </a>
        """
        result = result + indicators + items + controls + "</div>"
        self.carousel_count = self.carousel_count + 1
        return result
    
    # As we can't use carousel with whatsapp, we will implement a new list more detailed
    def create_detail_list( self, itemsArray ):
        items = "\n"
        for item in itemsArray:
            items = items + "*_" + item['name'] + ":_* " + item['description'] + "\n"
        return items

    # Add carousel to existing html
    def merge_carousel( self, html, carousel ):
        result = html.replace("$$$carousel$$$", carousel)
        return result
    
    # Adapt generic response to asked requirement
    def merge_text( self, html, requirementJSON, channel ):
        out = "$$$*$$$"
        result = html
        for key,value in requirementJSON.items():
            out = out.replace("*",key)
            if isinstance(value,list):
                value = self.create_list(value, channel)
            try:
                result = result.replace(out,value)
            except:
                print("Cant replace ",out)
            out = "$$$*$$$"
        return result