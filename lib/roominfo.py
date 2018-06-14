
class RoomInfo:
    """A structure for storing scraped room info in a consistent way"""
    property_name = None
    property_type = None
    bedroom_count = None
    bedroom_label = None
    amenities = []

    def prettyprint(self):
        print("= Property name")
        print("   - "+self.property_name)
        print()
        print("= Property type")
        print("   - "+self.property_type)
        print()
        print("= Number of bedrooms")
        print("   - {0} ({1})".format(self.bedroom_count,self.bedroom_label))
        print()
        print("= Number of bathrooms")
        print("   - {0} ({1})".format(self.bathroom_count,self.bathroom_label))
        print()
        print("= Amenities")

        for amenity in self.amenities:
            print("   - "+amenity)
