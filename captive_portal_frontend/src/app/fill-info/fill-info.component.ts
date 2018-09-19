import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { InfoService } from '../info.service';
import { ConnectionService } from '../connection.service';
import { CookieService } from 'ngx-cookie-service';
declare var $: any;


@Component({
  selector: 'app-fill-info',
  templateUrl: './fill-info.component.html',
  styleUrls: ['./fill-info.component.css'],
  providers: [InfoService, ConnectionService, CookieService]
})
export class FillInfoComponent implements OnInit {

  constructor(private infoService: InfoService, private connectionService: ConnectionService, private cookie: CookieService, private router: Router) { }

  ngOnInit() {
  
  }

  finishButtonAction(){
    var userNameInput = $("#name").val();
    var isStudentInput = $("input:radio[name='role']:checked").val();
    var currentClassInput = $("#current_class").val();
    var addressInput = $("#address").val();
    var phoneInput = $("#phone").val();
    var needInput = $("#need").val();

    var newInfo = {
      name: userNameInput,
      is_student: isStudentInput,
      current_class: currentClassInput,
      address: addressInput,
      phone: phoneInput,
      need: needInput
    }

    this.infoService.addInfo(newInfo, $);

   
  }

  showClass(){
    $('#classContent').show();
  }

  hideClass(){
    $('#classContent').hide();
  }


}
