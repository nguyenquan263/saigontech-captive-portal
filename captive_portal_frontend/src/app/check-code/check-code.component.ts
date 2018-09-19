import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { InfoService } from '../info.service';
import { ConnectionService } from '../connection.service';
import { CookieService } from 'ngx-cookie-service';
declare var $: any;

@Component({
  selector: 'app-check-code',
  templateUrl: './check-code.component.html',
  styleUrls: ['./check-code.component.css'],
  providers: [InfoService, ConnectionService, CookieService]
})
export class CheckCodeComponent implements OnInit {

  constructor(private info: InfoService, private connection: ConnectionService, private cookie: CookieService) { }

  ngOnInit() {
  }

  finishButtonAction() {
    var digit = $('#digit').val();
    var validDigit =
      {
        validate_number: digit
      }

    this.info.checkDigit(validDigit, $);
  }

}
