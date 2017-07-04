from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import random
app = Flask(__name__)

all_pants = [
    {
        "url": "https://www.amazon.com/gp/product/B06X92D246/ref=s9_acsd_al_bw_c_x_1_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/71bzQoRnuSL._UL1500_.jpg",
        "name":"PARIS SUNDAY Women's Sleeveless Romper",
        "price":"$44.50"
    },
    {
        "url": "https://www.amazon.com/gp/product/B06XKNJWF7/ref=s9_acsd_al_bw_c_x_2_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/81Ky0gTcPFL._UL1500_.jpg",
        "name":"MINKPINK Women's Paradise Printed Cropped Jumpsuit",
        "price":"$109.00"
    },
    {
        "url": "https://www.amazon.com/gp/product/B06ZZY1GCG/ref=s9_acsd_al_bw_c_x_3_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/71ECgY4zsCL._UL1500_.jpg",
        "name":"Pam & Gela Women's Strappy Romper",
        "price":"$225.00"
    },
    {
        "url": "https://www.amazon.com/gp/product/B06Y939QPP/ref=s9_acsd_al_bw_c_x_4_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/81r7Pc8V77L._UL1500_.jpg",
        "name":"Moon River Women's Floral Print Cold Shoulder Ruffle Romper",
        "price":"$75.00"
    },
    {
        "url": "https://www.amazon.com/gp/product/B06XTYV564/ref=s9_acsd_al_bw_c_x_5_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/81cBWSL8IbL._UL1500_.jpg",
        "name":"BCBGMAXAZRIA Women's Tyra Scarf Printed Romper",
        "price":"$198.00"
    },
    {
        "url": "https://www.amazon.com/gp/product/B01NAH9YLA/ref=s9_acsd_al_bw_c_x_7_w?ie=UTF8&pd_rd_r=NP1AG1PXK88C6Y8T3FAX&pd_rd_w=qjwl3&pd_rd_wg=vimHR&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_r=NP1AG1PXK88C6Y8T3FAX&pf_rd_t=101&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_p=3709846b-9110-478f-b42d-20a21b641639&pf_rd_i=16927296011",
        "imgurl":"https://images-na.ssl-images-amazon.com/images/I/71L988teeNL._UL1500_.jpg",
        "name":"BB Dakota Women's Tara Floral Print Crepe Jumpsuit",
        "price":"$74.99"
    }
];

@app.route("/summer", methods=['GET'])
@cross_origin()
def index():
    return jsonify(random.choice(all_pants))
