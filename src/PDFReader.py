import os
import pdfplumber
import csv

enstat = "click \"Contact the Seller.\""
headers = ['OrderNumber', "Pet Names", "SKU", "Color", "Line1",
           "line2", "line3", "line4", "line5"]


class PDFReader:
    def __init__(self, fd, cvs_name):
        self.fd = fd
        self.cvs_name = cvs_name

    def open_pdf(self):
        # Open pds
        count = 0
        os.chdir("./UnProccessedFiles")
        # Holds each customer order
        all_customers = []
        for files in self.fd:
            with pdfplumber.open(files) as pdf:
                # This will hold all the details of each order
                order = []
                for i in range(len(pdf.pages)):
                    
                    # Extract each of the pages
                    content = pdf.pages[i].extract_text().split('\n')
                    
                    # Checks if the end of the page has been reach, if not then add the next page to the order
                    if enstat in content[len(content)-1]:
                        order.extend(content)
                    
                        init_details = self.find_order_num(order)
                    
                        # total_order_list = self.find_total_order(order)
                        order_details = self.subOrder(order)
                        order_details.parse_each_order()
                        customer = CustomerOrder(init_details, order_details.pet_name, order_details.sku,
                                                order_details.line1, order_details.line2,
                                                order_details.line3, order_details.line4, order_details.line5,
                                                order_details.color)
                        print(customer)
                        all_customers.append(customer)
                        # now that a customer has been stored and we reached the final order, we must reset order
                        order = []
                        count += 1
                    else:
                        order.extend(content)
        print(count)
        self.write_to_csv(all_customers)

    def write_to_csv(self, customers):
        import os.path
        os.chdir("../ProccessFiles")
        with open(self.cvs_name, 'w', newline="", encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in customers:
                writer.writerow(i.finalOrder)
        f.close()

    # def find_total_order(self, array):
    #     total_order_list = []
    #     for i in range(0, len(array)):
    #         if "Grand total:" in array[i]:
    #             return total_order_list
    #         else:
    #             total_order_list.append(array[i])

    #     return total_order_list

    def subOrder(self, array):
        order_list = []
        temp = []
        line = False
        for i in array:
            # case when there is another order
            if line and "Line " not in i:
                order_list.append(temp)
                line = False
                temp = [i]

            # Case for the first line
            elif not line and "Line " in i:
                line = True
                temp.append(i)
            else:
                temp.append(i)
    
        order_list.append(temp)

        return Track(order_list)

    def find_order_num(self, array):
        temp = []
        for i in array:
            if "Thank you" in i:
                break
            else:
                temp.append(i)
        order = temp[len(temp) - 1].split(' ')[2]
        return [order]

sep = " --- "

class CustomerOrder:
    def __init__(self, init_details, pet_name, sku, line1, line2, line3, line4, line5, color):
        self.finalOrder = []
        self.finalOrder.extend(init_details)
        self.finalOrder.append(sep.join(pet_name))
        self.finalOrder.append(sep.join(sku))
        self.finalOrder.append(sep.join(color))
        self.finalOrder.append(sep.join(line1))
        self.finalOrder.append(sep.join(line2))
        self.finalOrder.append(sep.join(line3))
        self.finalOrder.append(sep.join(line4))
        self.finalOrder.append(sep.join(line5))
# This class Tracks each order
class Track:

    def __init__(self, order_list):
        self.order_list = order_list
        self.pet_name = []
        self.sku = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []
        self.color = []
        self.order_id = []

    # This function parses each order and appends it to its specific self.var
    def parse_each_order(self):
        for orders in self.order_list:
            SKU = "SKU: "
            FONT = "Font Color: "
            PETNAME = "Pet Name:"
            LINE1 = "Line 1:"
            LINE2 = "Line 2:"
            LINE3 = "Line 3:"
            LINE4 = "Line 4:"
            LINE5 = "Line 5:"

            for order in range(len(orders)):
                if SKU in orders[order]:
                    self.sku.append(orders[order].split(" Tax")[0].split("SKU: ")[1].split(" ")[0])
                elif FONT in orders[order]:
                    self.color.append(orders[order].split("Font Color: ")[1].split(" (")[0])
                elif PETNAME in orders[order]:
                    self.pet_name.append(orders[order].split("Pet Name: ")[1])
                elif LINE1 in orders[order]:
                    self.line1.append(orders[order].split("Line 1: ")[1])
                elif LINE2 in orders[order]:
                    self.line2.append(orders[order].split("Line 2: ")[1])
                elif LINE3 in orders[order]:
                    self.line3.append(orders[order].split("Line 3: ")[1])
                elif LINE4 in orders[order]:
                    self.line4.append(orders[order].split("Line 4: ")[1])
                elif LINE5 in orders[order]:
                    self.line5.append(orders[order].split("Line 5: ")[1])
                else:
                    continue

    # This functions prints the all the variables in self
    def print_self(self):
        print(self.pet_name)
        print(self.sku)
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.color)
        print(self.order_id)

