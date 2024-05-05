# 2D GUI using Pyqt5

This README.md will explain the implementation code for the 2021 NHIS 2D GUI created using Pyqt5.

Before using this GUI it is important to make sure you have the Pyqt5 package installed to your computer. To do so, you may type in the command: py -m pip install pyqt5, into your terminal. 

To load the GUI you may open a terminal on your computer and type: py pip path-to-NHIS2021_2D_GUI-folder/Main.py. Alternatively, you may load the Python classes from the NHIS2021_2D_GUI folder in this GitHub repository into a code editor, such as VSCode, and run the Main.py class from there.

## ChiSquare2Var.py

We import necessary modules from the Pyqt5 library: QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QLineEdit, Qt, and QFont

### class ChiSquare2Var(QWidget):

ChiSquare2Var passes in QWidget which is a base class for all GUI objects in Pyqt5. It provides functions like creating a window where you can place buttons, labels, text, and other Pyqt5 supported elements.

#### def __init__(self, data):
In our constructor *__init__()*, we create class attributes called *data* and *labels*. The attribute called *data* represents the dataset of our chi-square test csv file while *labels* represents a dictionary of labels which will eventually hold the columns *dep_x_squared*, *dep_p_value*, *anx_x_squared*, and *anx_p_value* from our chi.csv file. We then set the window flags to stay on top in order to ensure that when we're clicking around in the main menu, our ChiSquare2Var window doesn't get pushed behind. Lastly, we initialize the user interface.

#### def init_ui(self):
In our *init_ui()* method we begin to initialize the components within the user interface. First, we declare a vertical layout which arranges the GUI elements vertically. Next, we create the label for our search box with a font of size 14. Inside of the search box, we place the defaulted text to "Enter specific format" to remind the user that they must enter the specific format as seen from the chi-csv file. This is also set to a font size of 14. Next we connect the searched text signal to the update_combo_box() method. This will essentially match the input from the search box to the items in the drop down box. Then, we add the created labels as a widget to the GUI layout. Next, we create a label for the text "or" which will indicate to the user that there is an alternative way of selecting a question combination. This label is aligned to be centered with a font size of 14, and then it is added as a widget to the GUI layout. Next, we create and add the label "Select the question combination:" and a drop down box as a widget on the GUI layout. By doing so, it allows the user to scroll through and select a question combination. These are both set to a font size of 14. Lastly we create a button that says "Submit" on it with a font size of 14 which calls the calculate_chi_square() method when clicked on. Next we create a label to display the results obtained from the calculate_chi_square() method with a font size of 14 and add it as a widget to the GUI layout. Then in order to ensure that our GUI elements that we have previously created and added are arranged in an organized manner we set the layout for all the widgets using the .setLayout() method. Next, we add in the options for our drop down box. Lastly, we set the window title to *ChiSquare2Var* and the width of the window to 450 pixels. 

#### def update_combo_box(self, text):
This method updates the option selected in the drop down box according to the text entered in the search box. 

#### def calculate_chi_square(self):
Our *calculate_chi_square()* method we check if the question combintation exists in the index of the dataset. If it does exist in the dataset, we locate the row corresponding to this question combination. Next we create an empty String which we will use to store our final formatted result. We iterate through the dictionary which contains the labels for *dep_x_squared*, *dep_p_value*, *anx_x_squared*, and *anx_p_value*. For each label in the dictionary, it gets their respective values from the row we decected earlier using the column names. It then appends the formatted text of label + value to the empty String we created. Then we set the text from our appended String as a widget for the selected question combination on the GUI layout. If the question combination does not exist in the dataset, a warning message box is displayed.

## DataSet.py

We import necessary libraries from Pandas 

### class DataSet:

#### def load_data(dataset_url, index_col=None):
We have a static method called *load_data()* which allows us to call this method from ourside of the class without having to create an instance of the DataSet class. This method uses the Pandas library to read in a csv file from a designated url address. It then returns the loaded data.

## Main.py

