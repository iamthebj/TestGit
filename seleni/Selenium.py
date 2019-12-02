from selenium import webdriver
import pandas as pd
import urllib.request

driver = webdriver.Firefox()
driver.minimize_window()
driver.get("https://stubcreator.com/w-2-form-2018/")


#driver.maximize_window()
#driver.fullscreen_window()
#driver.minimize_window()

id_list =["w2_employer_address", "w2_ssn", "w2_employer_ein","w2_cnt_number","w2_emp_fname",
          "w2_emp_lname","w2_employe_address", "w2_state", "w2_esid", "w2_sswt", "w2_ssit",
           "w2_slwt","w2_slit","w2_sln", "w2_wtoc" ,"w2_fitw", "w2_ssw", "w2_sstw", "w2_mwt","w2_mtw", "w2_sst", "w2_at",
           "w2_vc", "w2_dcb", "w2_np", "w2_siba1", "w2_siba2", "w2_sibb1", "w2_sibb2","w2_sibc1","w2_sibc2" ,"w2_sibd1",
           "w2_sibd2", "w2_se", "w2_rp", "w2_tpsp", "w2_other"]

data = pd.read_csv("People_data_2018_500.csv")
rows_count = data.shape[0]
counter = 335
for j in range(334,400):
  id_box = driver.find_element_by_id("w2_employer_email")
  id_box.send_keys("abc@abc.com")
  for i in range(len(id_list)):
      id_box = driver.find_element_by_id(id_list[i])
      name = data.iloc[j,i]
      name = str(name)
      if id_list[i] == "w2_is_void" or id_list[i] == "w2_se" or id_list[i] == "w2_rp" or id_list[i] == "w2_tpsp":
        if name == 'True':
            #id_box.clear()
            id_box.click()
      else:
        name = str(name)
        id_box.send_keys(name)
  id_box = driver.find_element_by_id('check_preview')
  id_box.click()
  driver.implicitly_wait(5000)
  driver.implicitly_wait(5000)
  ele2 = driver.find_element_by_xpath("//ul[@id = 'w2form_slider2']/li[2]/img").get_attribute('src')
  ele3 = driver.find_element_by_xpath("//ul[@id = 'w2form_slider2']/li[3]/img").get_attribute('src')
  driver.close()
  
  driver = webdriver.Firefox()
  driver.minimize_window()
  driver.get("https://stubcreator.com/w-2-form-2018/")  

  file_name2 = "People_data_2018_1-500_20Sept_data_" + str(counter) + "a.jpg"
  file_name3 = "People_data_2018_1-500_20Sept_data_" + str(counter) + "b.jpg"
  urllib.request.urlretrieve(ele2, file_name2)
  print("Saving ", file_name2)
  urllib.request.urlretrieve(ele3, file_name3)
  print("Saving ", file_name3)
  counter += 1
driver.close()
print("Done")