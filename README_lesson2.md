# Контроль версий DEEP (GIT) (семинары)

![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/GitHub_Cat.webp)

* Работа с изменениями 

* Задание 
1. Просмотрите историю коммитов в своём проекте и выберите три случайных коммита. Просмотрите изменения, которые были в них сделаны.
2. Верните эти изменения командой git revert последовательно, чтобы в итоге получилось тоже три коммита.
3. Попробуйте отменить эти три коммита:
 последний — командами git reset --soft и git restore;
 предпоследний — командой git reset --mixed и git restore;
 первый — командой git reset --hard.

* Команда git reset --hard— это мощная и потенциально опасная команда в Git, которая          используется для сброса текущей ветки до определенного коммита.
git reset --hard это команда, которая позволяет вам перемещать указатель ветки и сбрасывать как промежуточную область, так и рабочий каталог, чтобы они соответствовали конкретной фиксации. Это мощная команда, которую следует использовать с осторожностью, поскольку она безвозвратно отбрасывает изменения и фиксации, которые происходят после указанной фиксации.

```
git reset --hard
```
*  git reset --mixed используется для сброса указателя HEAD ветки на конкретную фиксацию при сохранении изменений этой фиксации в рабочем каталоге,
Сбрасывает промежуточную область: --mixedпараметр in git reset --mixed является поведением по умолчанию, если параметр не указан. Он сбрасывает промежуточную область (индекс) в соответствии с указанным коммитом, отбрасывая любые промежуточные изменения, но сохраняя изменения в рабочем каталоге.
```
git reset --mixed
```
* git reset --soft гарантирует, что изменения, внесенные указанной фиксацией, сохраняются в    проомежуточной области (индексе). 
 Эта команда полезна , когда вы хотите изменить или повторно зафиксировать изменения из указанной фиксации.
```
git reset --soft
```
* git restore используется для восстановления файлов или каталогов в вашем рабочем каталоге до предыдущего состояния. Это позволяет вам отменить изменения, внесенные в файлы или каталоги, либо восстановив их до состояния последней фиксации, либо отменив локальные изменения.
```
git restore 
```
* git reset @~ один Коммит назад




 * 2 Верните эти изменения командой git revert последовательно, чтобы в итоге получилось тоже  три коммита.
![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/1_git_revert_3commit.png)



* 3  Отменим эти 3 коммита:
    последний — командами git reset --soft и git restore;


![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/2_reset_soft.png)

![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/3_Restore_staged.png)

 * предпоследний — командой git reset --mixed и git restore;

![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/4.png)



* первый — командой git reset --hard.

![DEEP_CONTROL_VERSION](https://github.com/DRain777/control_version_deep/blob/main/python_shell/source/5.png)











    















