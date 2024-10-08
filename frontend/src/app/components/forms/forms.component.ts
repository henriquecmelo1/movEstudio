import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import { StudentService } from '../../services/student.service';
import { Router, RouterLink } from '@angular/router';


@Component({
  selector: 'app-forms',
  standalone: true,
  imports: [ CommonModule, FormsModule, ReactiveFormsModule, RouterLink  ],
  templateUrl: './forms.component.html',
  styleUrl: './forms.component.css'
})
export class FormsComponent implements OnInit {

  userForm!: FormGroup;

  
  constructor(
    private fb: FormBuilder, 
    private studentService: StudentService,
    private router: Router
  ) {}
  

  
  ngOnInit(): void {
    this.userForm = this.fb.group({
      cpf: ['', [Validators.required, Validators.pattern('[0-9]{11}')]],
      name: ['', Validators.required],
      birthday: [''],
      cellphone: ['', [Validators.required, Validators.pattern('[0-9]{11}')]],
      payment_day: ['', [Validators.min(1), Validators.max(31)]],
      payment_value: [''],
      frequency: ['',  Validators.min(1)],
      appointments: [''],
      emergency_contact: ['']
    });

    // birthday default value
    const today = new Date().toISOString().split('T')[0];
    this.userForm.patchValue({ birthday: today });

    // payment_day default value
    this.userForm.patchValue({ payment_day: 1 });

    // payment_value default value
    this.userForm.patchValue({ payment_value: 0 });

    // frequency default value
    this.userForm.patchValue({ frequency: 1 });

    
  };


  onSubmit(form: any) {
    console.log(form.value)
    if (form.valid) {
      this.studentService.createStudent(form.value).subscribe(response => {
        console.log('Student created successfully', response);
        this.router.navigate(['/home'])
      }, error => {
        console.error('Error creating student', error);
      });

      
      
    }
  };

}
