import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { StudentService } from '../../services/student.service';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-display',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './display.component.html',
  styleUrl: './display.component.css'
})
export class DisplayComponent implements OnInit {

  editStudentForm: FormGroup;
  currentStudent: any;

  constructor(private fb: FormBuilder, private studentService: StudentService) {
    this.editStudentForm = this.fb.group({
      cpf: ['', Validators.required],
      name: ['', Validators.required],
      birthday: ['', Validators.required],
      cellphone: ['', Validators.required],
      payment_day: ['', Validators.required],
      payment_value: ['', Validators.required],
      frequency: ['', Validators.required],
      appointments: ['', Validators.required],
      emergency_contact: ['', Validators.required]
    });
  }


  students: any[] = []
  search: string = '';

  ngOnInit() {
    this.studentService.getStudents().subscribe((data: any) => {
      this.students = data;
    });
  }
  onSubmitSearch() {
    this.studentService.filterStudents(this.search).subscribe((data: any) => {
      this.students = data;
    });
  }
  deleteStudent(cpf: any) {
    this.studentService.deleteStudent(cpf).subscribe((data: any) => {
      this.students = data;
      window.location.reload();
    });
  }
  
  openEditModal(student: any) {
    this.currentStudent = student;
    this.editStudentForm.setValue({
      cpf: student.cpf,
      name: student.name,
      birthday: student.birthday,
      cellphone: student.cellphone,
      payment_day: student.payment_day,
      payment_value: student.payment_value,
      frequency: student.frequency,
      appointments: student.appointments,
      emergency_contact: student.emergency_contact
    });
  }

  editStudent() {
    this.studentService.updateStudent(this.editStudentForm.value).subscribe((data: any) => {
      this.students = data;
      window.location.reload();
    });
  }
   

}
